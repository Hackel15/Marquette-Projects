#Comments are written by the modified lines of code.
#I tried to preserve your logic and minimize any large changes.
#(Make sure to change the file locations at the bottom of this file)

import string

def xor(nameIn, nameOut, key):
    toDecode = bytearray()
    result = bytearray()
    with open(nameIn, "rb") as inFile, open(nameOut, "wb") as outFile:
        for line in inFile:
            for x in line:
                toDecode.append(x)
        for i in range(len(toDecode)):
            result.append(toDecode[i] ^ ord(key[i%len(key)]))
        outFile.write(result)
#r1c2rd3 h4ch


#Function purpose: Read file and returns the length of key
#Parameters: nameIn-->File being read
def length(nameIn):
    #VARIABLES
    dicta={}
    
    with open(nameIn, 'rb') as f1:
        results=bytearray()
        for line in f1:
            for x in line:
                results.append(x)
        
        for i in range(15): # <-- Your loop checks possible key lengths of a certain range. 
                            #Use a smaller value (i.e. 15)
            count=0
            for c in results:
                if results[i]==c:
                    count+=1
            dicta[i]=count
        print ("KEY LENGTH  |  FREQENCY")
        for item,value in dicta.items():
            print('{:<15}{:<}'.format(item, value))
            
        return max(dicta, key=dicta.get) #Returns the highest (max) counted key length
                                         #This value will be used in your defined fog() function


#Function purpose: Searches for key values.
#Parameters: keyLength-->Length of key, nameIn-->File being read
def fog(keyLength, nameIn):
    #VARIABLES
    dictb={}
    encodedValues = [] #Stores individual values of encrypted message
    frequencies = []   #Stores coincidences for (n)+k (k = keyLength, n = the range of keyLength)
    foundKeyValue = [] #Stores the numerical representation of the key

    #Don't really need these assignments
    for letter in string.ascii_lowercase:
        dictb[letter]=0
    for number in string.digits:
        dictb[number]=0
    for char in string.punctuation:
        dictb[char]=0
    for space in " ":
        dictb[space]=0
        
    with open(nameIn,'rb') as f: #Read file into a list
        for line in f:
            for number in line:
                encodedValues.append(number)
            
##      Next.. count coincidences for the key length values.
##      For example: If the key length is equal to length 'k'.
##                   Count coincidences for (n)+k ... until (n)==k.
##                   Where 'n' is in range(0, keyLength).             
##      See code below...
        for index in range(keyLength):
            dictb = {} #Need to reinitialize dictionary each time 
            for val in encodedValues[index::keyLength]:#Step through the encrypted message by the key length
                if val in dictb.keys(): #Counts additional coincidences
                    dictb[val] += 1
                else:                   #Initializes a 'key' if it does not exist in dictionary
                    dictb[val] = 1
            frequencies.append(dictb) #Append the dictionary to the list for each index of the key length

##      Similar to the length function above we need to find the max value of the dictionary.
##      However, we have a 'list' of 'dictionaries' so we need to use a 'for loop'.
##      After finding the most frequent value, we XOR it with the most frequent value in the
##      English language, the 'space' (' ').  This will undo or decrypt the key.

        for dic in frequencies:
            foundKeyValue.append( max(dic, key=dic.get) ^ ord(' ') )
        
        print ('\nKEY LENGTH: ', keyLength, '\nKEY: ', end = "")
        for key in foundKeyValue:
            print ( chr(key) , end = "")

            
##        for letter in line.lower():
##            if letter in string.ascii_letters:
##                dictb[letter]+=1
##        for number in line.lower():
##            if number in string.digits:
##                dictb[number]+=1
##        for char in line.lower():
##            if char in string.punctuation:
##                dictb[char]+=1
##        for space in line:
##            if space in " ":
##                dictb[space]+=1
##    count = 0
##    dictc = {}
##    for i in range (1,250000):
##        if i in dictb.values():
##            count += i
##    return dictb, count


fog(length("bla.txt"),"bla.txt")
#Now use the found key to decrypt the message.
#The process is similar to the code Dr. Jain provided for encrypting a message
#Good luck

