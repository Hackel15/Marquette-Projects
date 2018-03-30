library(ggmap)
library(ggplot2)
library(maptools)
library(datasets)
library(maps)
library(plyr)
library(reshape2)
install.packages("maps")
library(maps)
library(maptools)

#Set working directory
setwd("C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\17-18_Spring\\Data Science\\Data")

#Read data
olympic_data <- read.csv("athletes.csv")
countries <- read.csv("mydata2.csv")
map <- map_data("world")
country_codes <- read.csv("Country_List_ISO_3166_Codes_Latitude_Longitude.csv")

#Calculate medal count
olympic_data$medalcount <- olympic_data$bronze + olympic_data$silver + olympic_data$gold
olympic_data$gold <- NULL
olympic_data$silver <- NULL
olympic_data$bronze <- NULL
olympic_data$id <- NULL
clean_data <- ddply(olympic_data,"nationality",numcolwise(sum))

#Sort data
sort(clean_data)
sort(olympic_data)
sort(countries)
olympic_data <- sort(unique(olympic_data$nationality))
olympic_data <- data.frame(olympic_data)
olympic_data$medals <- clean_data

#Tidy data
country_codes$Alpha.3.code[1]
country_codes$Alpha.3.code <- (trimws(country_codes$Alpha.3.code))
clean_data$nationality <- (trimws(clean_data$nationality))
typeof(country_codes$Alpha.3.code[1])
typeof(clean_data$nationality[1])

#Convert ISO Alpha-3 to Country name
country_codes$Country[match("AFG" , country_codes$Alpha.3.code)]
clean_data$nationality <- country_codes$Country[match(unlist(clean_data$nationality) , country_codes$Alpha.3.code)]
clean_data$nationality <- na.omit(clean_data$nationality)
clean_data

#Use look-up table to find latitude and longitude coordinates
clean_data$lat <- country_codes$Latitude..average.[match(unlist(clean_data$nationality) , country_codes$Country)]
clean_data$long <- country_codes$Longitude..average.[match(unlist(clean_data$nationality) , country_codes$Country)]


# We needed to rearrange our data in order to produce the following choropleth graphs.
# The nationality column of our dataset displays country code names in ISO Alpha-3 format, a three letter
# country identifier.  To make our graph we needed to convert this format to its respective country name,
# and gather the coordinate data for accurate plots.  After searching for resources, we found a look-up 
# table that we crossreferenced to match each country competing in the Rio Olympics.  One problem we discovered
# in our data were the mislabled ISO Alpha-3 codes.  There were inconsistencies within this column that
# did not follow the standardized labling format.  In result, 25 countries were unable to be plotted.  However,
# after further inspection, we found that the 25 mislabled countries held very low results for players sent
# by country and number of medals won.  

#Rename columns
clean <- subset.data.frame(clean_data, select = c("nationality", "medalcount", "lat", "long"))
colnames(clean) <- c("Country", "Count", "Lat", "Long")

# Load map data as dataframe
map <- map_data("world")

# Look at the map data
head(map)

# Load dplyr
library(dplyr)

write.csv(clean, file = "My_Medal2.csv")
clean <- read.csv("My_Medal2.csv")

# Join countries and map data
countries2 <- clean %>%
  left_join(map, 
            by = c("Country" = "region")) %>%
  select(
    Country, 
    Longitude = long, 
    Latitude = lat, 
    Group = group,
    Order = order,
    Count) %>%
  arrange(Order) %>%
  as.data.frame()

#Look at countries2
tail(countries2)

# Create a choropleth
ggplot(
  data = countries2) + 
  borders(
    database = "world",
    colour = "grey60",
    fill = "grey90") +
  geom_polygon(
    aes(
      x = Longitude, 
      y = Latitude, 
      group = Group,
      fill = Count), 
    color = "grey60") +
  scale_fill_gradient(
    low = "white",
    high = "red") +
  ggtitle("Medals Won by Country") +
  xlab("") +
  ylab("") +
  labs(color = "Medals") +
  theme(
    panel.background = element_blank(),
    axis.title.x=element_blank(),
    axis.text.x=element_blank(),
    axis.ticks.x=element_blank(),
    axis.title.y=element_blank(),
    axis.text.y=element_blank(),
    axis.ticks.y=element_blank())
