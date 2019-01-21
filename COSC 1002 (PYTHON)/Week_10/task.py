import random

def start(file):
      rand = random.randrange(len(file)-1)
      while ((file[rand].isalpha() == False) | (file[rand+1].isalpha() == False)):
            rand = random.randrange(len(file)-1)
      return rand
      
def search(file, index, key):
      index = file.find(key, index)
      while ((index < 0) | (file[index].isalpha() == False) | (file[index+1].isalpha() == False)):
            index = file.find(key, random.randrange(len(file)-1),)
      return index+1
      

def getPass(file, password):
      while(len(password) < 12):
            index = search(file, random.randrange(len(file)-1), password[len(password)-1])
            password += file[index]
      return password

def check(select, passwords):
      for p in passwords:
            if select == p:
                  print("Success")
                  return True
      print("Invalid password")            
      return False

inFile = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_10\\doc.txt"
fileArray = ""
passwords = []
index = 0

with open(inFile, 'r') as file:
      for line in file:
            for letter in line:
                  fileArray += letter

for x in range(10):
    index = start(fileArray)
    passwords.append(fileArray[index] + fileArray[index+1])
    passwords[x] = getPass(fileArray, passwords[x])

print('{:^25}\n{:}'.format("PASWORDS", 25*"-"))
for p in passwords:
      print('{:^25}'.format(p))

selected = input('\nChoose password: ')
while ( check(selected, passwords) is False ):
      selected = input('\nChoose password: ')
      
            
      
            

