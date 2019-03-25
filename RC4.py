#!/usr/bin/env python
#
#  Anne-Marie Oelschlager
#  RC4.py
#	 A simple program to encrypt an input file with RC4.
#

import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

def main(): 

	# process command line arguments
	if len(sys.argv) < 3:
		print("Usage: fileEncrypt.py key iv file")
		sys.exit()		

	# 1. file
	name = sys.argv[1]
	print("filename: %s" % name)

	# 2. key
	key = sys.argv[2]
	print("key: %s" % key)

	# open files	
	try:
		inFile = open(name, 'r')
		outFile = open(name + '.rc4', 'w')

	except IOError:
		print("Error: could not open file: %s" % name )
		sys.exit()
	
	# save data in inFile
	data = inFile.read()
	
	# save hex key to bytes
	keyBytes = bytes(bytearray.fromhex(key))
	
	# prep cipher	
	cipher = Cipher(algorithms.ARC4(keyBytes), mode=None, backend=backend)

	# encrypt plain text
	encryptor = cipher.encryptor()
        ct = encryptor.update(data)
	outFile.write(ct)

	# closed files
	inFile.close()
	outFile.close()

	return 0

if __name__ == '__main__': 

	main()
