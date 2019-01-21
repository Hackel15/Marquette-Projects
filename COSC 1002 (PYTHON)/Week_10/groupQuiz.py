import string
import re

def count():
      file = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_10\\lab.py"
      count = 0
      try:
            with open(file) as f:
                  for line in f:
                        for word in re.split('\W+', line):
                              if word == "range":
                                    count += 1
            return count
      except FileNotFoundError:
            print("Fiile ", file, "could not be found.")

count()
