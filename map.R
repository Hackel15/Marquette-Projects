#install packages
install.packages("maps")
install.packages("gglot2")
install.packages("ggmap")
#load GGPlot2
library(ggmap)
library(ggplot2)
library(maptools)
library(datasets)
library(maps)
library(plyr)
library(reshape2)

#Set working directory
setwd("C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\17-18_Spring\\Data Science\\Data")


#TEST
olympic_data <- read.csv("athletes.csv")
country_codes <- read.csv("countries_codes_and_coordinates.csv")
countries <- read.csv("mydata2.csv")

sort(olympic_data)
sort(countries)

table(olympic_data$nationality)
tab <- table(olympic_data$nationality, olympic_data$medalcount)
tab

olympic_data <- sort(unique(olympic_data$nationality))
olympic_data <- data.frame(olympic_data)
olympic_data$medals <- clean_data

olympic_data
countries

countries$lat <- country_codes$Latitude..average.[match(unlist(countries$Var1) , country_codes$Alpha.3.code)]
countries$long <- country_codes$Longitude..average.[match(unlist(countries$Var1) , country_codes$Alpha.3.code)]

countries$Var1 <- country_codes$Country[match(unlist(countries$Var1) , country_codes$Alpha.3.code)]
countries <- na.omit(countries)

mp <- NULL

mapworld <-  borders("world", colour="gray50", fill="gray50") # create a layer of borders
mp <- ggplot() +   mapworld

mp <- mp + geom_point(aes(x=countries$long, y=countries$lat) ,color="blue", size=1)
mp

colnames(countries) <- c("Index", "Country" ,"Count","Latitude","Longitude")


# Load map data as dataframe
map <- map_data("world")

# Look at the map data
head(map)

# Load dplyr
library(dplyr)

# Join countries and map data
countries2 <- countries %>%
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
#write.csv(countries, file = "MyData2.csv")

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
  ggtitle("Count of Athletes by Country") +
  xlab("") +
  ylab("") +
  labs(color = "Athletes") +
  theme(
    panel.background = element_blank(),
    axis.title.x=element_blank(),
    axis.text.x=element_blank(),
    axis.ticks.x=element_blank(),
    axis.title.y=element_blank(),
    axis.text.y=element_blank(),
    axis.ticks.y=element_blank())
