#DECRYPTION FOR A CEASER CIPHER ENCRYPTION

####VARIABLES####
encodedNums = []
myFreq = {}
frequencies = []
keyNumbers = []
encodedText = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\17-18_Spring\\Computer Security\\Project1\\Project1\\challenge5.txt"

#Display current coded message
print ("DECODING -> TEXT FILE: ", encodedText, "\n")

####METHODS####

#Decrypt the message
def decrypt (encoded, shift):
      message = ''

      for letter in range(100):
            k = (ord(encoded[letter])+shift) % 26 + 65
            if k < 65:
                  k += 65
            message += chr(k)
      print(message)
            
    
#Opens and reads encrypted message
with open(encodedText, 'r', encoding="utf-8") as file:
    for line in file:
        for letter in line:
            encodedNums.append(letter)

for i in range(0, 26):
      print(chr(i + 65) + ": ", end="")
      decrypt(encodedNums, i)
