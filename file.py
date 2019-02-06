#Works in Python2.7 
import sys

file = open(sys.argv[1],'rb')

#print filename first
print(sys.argv[1]+":"),

#Check if ELF File
magic = ['7f', '45', '4c', '46']
bytes = file.read(4)  # read first 4 bytes 
bytes = ["{:02x}".format(ord(c)) for c in bytes]

if cmp(magic,bytes) == 0:
	print("ELF"),
else:
	print("NOT ELF! QUITTING !")
	sys.exit()

#check if 32 bit or 64 bit
byte = ord(file.read(1)) #read 1 byte
if byte == 1:
	print("32-bit"),
else:
	print("64-bit"),

#check Endianess

byte = ord(file.read(1)) #read 1 byte
if byte == 1:
        print("LSB"),
else:
        print("MSB"),


file.close()
