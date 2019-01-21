from pyDes import *

k = des(b"An1Ta666", CBC, b"\0\0\0\0\0\0\0\0", pad=" ", padmode=PAD_NORMAL)
registro="Thomas Schwarz, Jesuit Community, Marquette University, Milwaukee, Wisconsin, USA, 4900."

def encrypt():
    fp=open("data.hex","wb")
    fp.write(k.encrypt(bytes(registro,encoding='latin-1')))
    fp.close()

def decrypt():
    fp = open("data.hex", "rb")
    cifra = fp.read(96)
    print(str(k.decrypt(cifra),encoding='latin-1'))
    fp.close()

#encrypt()
decrypt()
