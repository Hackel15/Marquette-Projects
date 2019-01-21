#Tyler Hackel
#Josie Zucca

text = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\17-18_Spring\\Algorithims II\\11-0.txt"

lineCount = -1
totalCount = 0
with open(text, 'r', encoding = "utf-8") as file:
    for line in file:
        lineCount += 1
        for i in range(0, len(line)):
            if line[i] == 'D':
                if line[i+1] == 'o':
                    if line[i+2] == 'd':
                        if line[i+3] == 'o':
                                print("Line: " + str(lineCount))
                                totalCount+=1
print("Total Matches: " + str(totalCount) + '\n')

lineCount = -1
state = 1
totalCount = 0
with open(text, 'r', encoding = "utf-8") as file:
    for line in file:
        lineCount+=1
        for i in line:
            if state == 1:
                if i == 'D':
                    state = 2
            elif state == 2:
                if i == 'o':
                    state = 3
                else:
                    state = 1
            elif state == 3:
                if i == 'd':
                    state = 4
                else:
                    state = 1
            elif state == 4:
                if i == 'o':
                    state = 5
                else:
                    state = 1
            if i == 'D':
                state = 2
            if state == 5:
                print("Line: " + str(lineCount))
                print(line)
                totalCount+=1
                state = 1
print("Total Matches: " + str(totalCount))
        
