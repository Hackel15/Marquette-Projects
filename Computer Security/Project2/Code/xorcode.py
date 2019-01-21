import random

registro=b"Thomas Schwarz, Jesuit Community, Marquette University, Milwaukee, Wisconsin, USA, 4900."
k = 14391

def encrypt():
    random.seed(k)
    with open("datax.hex","wb", buffering=0) as outfile:
        output = bytearray()
        for i in range(len(registro)):
            output.append(registro[i]^random.randint(0,255))
        outfile.write(output)
            
            
def decrypt():
    random.seed(k)
    buffer = bytearray(len(registro))
    with open("datax.hex","rb") as infile:
        infile.readinto(buffer)
        for i in range(len(registro)):
            buffer[i] = buffer[i]^random.randint(0,255)
        print(str(buffer))

encrypt()
decrypt()
