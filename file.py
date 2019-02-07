#Works in Python2.7 
import sys
import struct 
file = open(sys.argv[1],'rb')

#print filename first
print(sys.argv[1]+":"),

#Check if ELF File
magic = ['7f', '45', '4c', '46']
bytes = file.read(4)  # read first 4 bytes 
bytes = ["{:02x}".format(ord(c)) for c in bytes]

if cmp(magic,bytes) == 0:
	print("Filetype: ELF")
else:
	print("NOT ELF! QUITTING !")
	sys.exit()

#check if 32 bit or 64 bit
byte = ord(file.read(1)) #read 5th byte for 1 byte
if byte == 1:
	print("32-bit")
else:
	print("64-bit")

#check Endianess

byte = ord(file.read(1)) #read 6th byte for 1 byte
if byte == 1:
        print("LSB")
else:
        print("MSB")

file.read(1) #read 7th byte, ( not processing this information, so just read )


#check the target operating system
print("Target Operating System: "),
byte = file.read(1)  # read 7th byte
byte = int(byte.encode('hex'),16)
if byte == 0x00:
	print("System V")
elif byte == 0x01:
	print("HP-UX")
elif byte == 0x02:
	print("NetBSD")
elif byte == 0x03:
	print("Linux")
elif byte == 0x04:
	print("GNU Hurd")
elif byte == 0x06:
	print("Solaris")
elif byte == 0x07:
	print("AIX")
elif byte == 0x08:
	print("IRIX")
elif byte == 0x09:
	print("FreeBSD")
elif byte == 0x0A:
	print("Tru64")
elif byte == 0x0B:
	print('Novell Modesto')
elif byte == 0x0C:
	print("OpenBSD")
elif byte == 0x0D:
	print("OpenVMS")
elif byte == 0x0E:
	print("NonStop Kernel")
elif byte == 0x0F:
	print("AROS")
elif byte == 0x10:
	print("Fenix OS")
elif byte == 0x11:
	print("CloudABI")
else:
	print("Unknown")

file.read(1) # read 8th byte
file.read(7) # read 9th byte, 7 bytes

#Object File type
bytes = file.read(2) # read 16th byte, 2 bytes
bytes = ["{:02x}".format(ord(c)) for c in bytes]

bytes = int(bytes[0],16)
if bytes == 0x00:
	print("No file type")
elif bytes == 0x01:
	print("Relocatable file")
elif bytes == 0x02:
	print("Executable file")
elif bytes == 0x03:
	print("Shared object file")
elif bytes == 0x04:
	print("Core file")
elif bytes == 0xfe00:
	print("Operating system-specific")
elif bytes == 0xfeff:
	print("Operating system-specific")
elif bytes == 0xff00:
	print("Processor-specific")
elif bytes == 0xffff:
	print("Processor-specific")
else:
	print("Unknown Object File Type")

bytes = file.read(2) # read 18th byte, 2 bytes
bytes = ["{:02x}".format(ord(c)) for c in bytes]
bytes[0]=int(bytes[0],16)
arch = bytes[0]
if bytes[0] == 0x00:
	print("No specific instruction set")
elif bytes[0] == 0x02:
	print("SPARC")
elif bytes[0] == 0x03:
	print("x86")
elif bytes[0] == 0x08:
	print("MIPS")
elif bytes[0] == 0x14:
	print("PowerPC")
elif bytes[0] == 0x16:
	print("S390")
elif bytes[0] == 0x28:
	print("ARM")
elif bytes[0] == 0x2A:
	print("SuperH")
elif bytes[0] == 0x32:
	print("IA-64")
elif bytes[0] == 0x3E:
	print("x86-64")
elif bytes[0] == 0xB7:
	print("AArch64")
elif bytes[0] == 0xF3:
	print("RISC-V")
else:
	print("Unknown Instruction Set")
file.read(4) #read 22th byte, 2 bytes

#Program Header

if arch == 0x03: #0x03 => x86
	bytes=file.read(4)
	bytes = ["{:02x}".format(ord(c)) for c in bytes]
	#print(bytes)
else:
	bytes=file.read(8)
	bytes = ["{:02x}".format(ord(c)) for c in bytes]
	#print(bytes)

file.close()
