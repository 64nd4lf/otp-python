import sys # to read command line arguments
from random import * # to generate random key
import timeit # to measure time taken to execute

start = timeit.default_timer() # starts timer

# converts text to binary
def toBinary(_str):
	return ''.join(bin(ord(x)) for x in _str).replace('b', '')

# performs xor between the key and the message bit by bit and returns the binary cipher
def enc(key, m):
	ciph = ''
	b_m = toBinary(m)
	for x in range (len(key)):
		ciph += str((int(key[x]) ^ int(b_m[x])))
	return ciph

#performs xor between the key and the cipher text and returns the message in binary
def dec(key, ciph):
	m = ''
	for x in range(len(key)):
		m += str((int(key[x]) ^ int(ciph[x])))
	return m

# generates a random key of length k
def keygen(k):
	key = ''
	for x in range(k):
		key += str(randint(0, 1))
	return key

def main(argv):
	# program enters the following segment if the enc command is used.
	if(argv[1] == "enc"):
		# load the key file
		f = open(argv[2], 'r')
		key = f.read()
		f.close()
		# load the plaintext file
		f = open(argv[3], 'r')
		message = f.read()
		f.close()
		# checks if the lengths of key and message match and performs encryption if true
		if((len(key))/8 == len(message)):
			cipher = enc(key, message)
			print (cipher)
			f = open(argv[4], 'w')
			f.write(cipher)
			f.close()
		else:
			print("Error: Length of key and message don't match")

	# program enters the following segement if dec command is used
	elif(argv[1] == "dec"):
		m_text = ''
		# load the key file
		f = open(argv[2], 'r')
		key = f.read()
		f.close()
		# laod the ciphertext file
		f = open(argv[3], 'r')
		ciph = f.read()
		f.close()
		# validates lengths of key and cipher
		if(len(key) == len(ciph)):
			message = dec(key, ciph)
			temp = int(message, 2)
			m_text = temp.to_bytes((temp.bit_length() + 7) // 8, 'big').decode()
			print(m_text)
			f = open(argv[4], 'w')
			f.write(m_text)
			f.close()
		else:
			print("Error: Length of key and cipher don't match")

	# program enters the following segment if keygen is used
	elif(argv[1] == "keygen"):
		key = keygen(int(argv[2]))
		# write the generated key into a file
		f = open(argv[3], 'w')
		f.write(key)
		f.close()

	else:
		print ("Error: Use enc or dec or keygen")

# validates minimum number of arguments
if(len(sys.argv)<4):
	print("Error: Invalid arguments")
main(sys.argv)

#stops the timer
stop = timeit.default_timer()
# measures the time difference to determine the time taken to execute
print (stop - start)