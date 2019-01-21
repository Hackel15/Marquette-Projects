#LAB 10
import random
import string

def nums(n):
      return [random.randrange(1, 7) for i in range(n) ]

def bools(n):
       tem = ""
       for b in n:
             if b:
                   tem += "*"
             else:
                   tem += " "
       return tem

def dna(line):
      dic = {}
      for letter in "ACGTWY":
            dic[letter] = 0
      for word in line:
            for letter in word:
                  if letter in "ACGTWY":
                        dic[letter] += 1
      return dic

def per():
      values = ["A", "T", "C", "G"]
      pers = []
      for first in values:
            for second in values:
                  pers.append(first+second)
      return pers

def search(line):
      values = per()
      dic = {}
      lineArray = list(line)
      for key in values:
            dic[key] = 0
            
      for index in range (0, len(lineArray)-1):
            key = lineArray[index]+lineArray[index+1]
            if key in values:
                  dic[key] += 1
      return dic


def hiv():
      inFile = 'C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_10\\HIV.txt'
      outFile = 'C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_10\\HIV_OUT.txt'
      fileList = []
      dic = {}
      lineCount = 0
      temp = ""
      with open(inFile, 'r') as iFile, open(outFile, 'w') as oFile:
            for line in iFile:
                  lineCount += 1
                  if lineCount % 2 == 1:
                        oFile.write(line)
                  else:
                        dic = dna(line)
                        count = 0
                        for key in dic:
                              temp = key + " " + str(dic[key]) + "\n"
                              oFile.write(temp)
                              count += dic[key]
                        oFile.write('Total Letters: ')
                        oFile.write(str(count)+'\n')
                        dic = search(line)
                        oFile.write('Permutations : \n')
                        for key in dic:
                              temp = key + " " + str(dic[key]) + "\n"
                              oFile.write(temp)
                        oFile.write('\n\n')
                  


print(nums(10))

print(bools([True, True, False, False, True]))

hiv()
