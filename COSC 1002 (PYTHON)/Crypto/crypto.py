#DECRYPTION FOR AN XOR ENCRYPTION WITH AN UNKNOWN KEY

####VARIABLES####
encodedNums = []
myFreq = {}
frequencies = []
keyNumbers = []
encodedText = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\17-18_Spring\\Computer Security\\Project1\\Project1\\challenge1.txt"

#Display current coded message
print ("DECODING -> TEXT FILE: ", encodedText, "\n")

####METHODS####

#Encrypt Message
def encrypt(key):
    inFile = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\16-17_Spring\\Computer\\Crypto\\in.txt"
    outputFile = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\16-17_Spring\\Computer\\Crypto\\secret.txt"
    message = bytearray()
    tempEncrypt = bytearray()
    with open(inFile, 'rb') as iFile, open(outputFile, 'wb') as oFile:
        for line in iFile:
            for letter in line:
                message.append(letter)
        for index in range (len(message)):
            tempEncrypt.append(message[index] ^ ord(key[index%len(key)]))
        oFile.write(tempEncrypt)
    
#Shifts data based on offset value
def shift(data, offset):
    return data[offset:]

#Counts matched value of original message and shifted message
def countMatches(a, b, keyLength):
    count = 0
    for index in range(keyLength, len(b)-keyLength):
        if a[index] == b[index]:
            count += 1
    return count

#Decrypt the message
def decrypt (encoded, key):
    message = ''
    for index in range (len(encoded)):
         message += (chr(encoded[index] ^ key[index%len(key)]))
    return message

#Opens and reads encrypted message
with open(encodedText, 'rb') as file:
    for line in file:
        for byte in line:
            encodedNums.append(byte)

#Search through possible key lengths
print ('{:10} | {:10}'.format("KEY LENGTH", "FREQENCY") + "\n" + 22 * "-")
for keyLength in range(3, 25): #ADJUST RANGE IF KEY LENGTH IS THOUGHT TO BE LARGER 
    freq = countMatches(encodedNums, shift(encodedNums, keyLength), keyLength)
    print ( "{:^10} | {:^10}".format(keyLength, freq))
    myFreq[keyLength] = freq

#Find the 5 highest counted matches
maxFreq = (sorted(myFreq, key=myFreq.get, reverse=True)[:5])

#Assign our best possible match for a key length
keyLength = maxFreq[0]

#Count coincidences in encoded message using key length
for i in range(0, keyLength):
    count = {}
    for asciiNum in encodedNums[i::keyLength]:
        if asciiNum in count.keys():
            count[asciiNum] += 1
        else:
            count[asciiNum] = 1
    frequencies.append(count)

#Create key using most frequently used value ' '
#For more difficult encryption, compare other high frequency letters: "e" 
for keyFreq in frequencies:
      key = max(keyFreq, key=keyFreq.get) ^ ord(' ')
      keyNumbers.append(key)

#Print the found key length and key
print ('\nKEY LENGTH: ', keyLength, '\nKEY: ', end = "")
for key in keyNumbers:
    print ( chr(key) , end = "")
    
print (end='\n')
print ('\nDecrypting Text')
print (decrypt(encodedNums, keyNumbers))
