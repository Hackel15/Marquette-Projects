def alice():
      file = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_7\\Alice.txt"
      line_count = 0
      with open(file, "rt", encoding = "utf-8") as f:
            for line in f:
                  line_count += 1
                  for word in line.split():
                        if (len(word) > 10):
                              for letter in word:
                                    if (letter in "zZ"):
                                          print (word)
      return line_count

def win_file(location):
      loc = ""
      for index in location:
            if index == "\\":
                  loc += "\\"
            else:
                  loc += index  
      return loc
            
      
def quiz(string):
      count = 0
      with open(string, "r", encoding = "utf-8") as f:
            for line in f:
                  for word in line.split():
                        count += 1
      return count
                        
      


