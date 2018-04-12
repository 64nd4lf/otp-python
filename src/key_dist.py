from random import *

# genarates random keys
def keygen(k):
	key = ''
	for x in range(k):
		key += str(randint(0, 1))
	return key

def main():
	count = 0
	freq = {}
	keys = []
	# loop to generate 5000 keys
	for x in range(5000):
		keys.append(keygen(3))
	unique_keys = set(keys)
	for x in unique_keys:
		for y in keys:
			if(y == x):
				count = count + 1
		# prints the key and it's corresponding frequency
		print(x, count)
		count = 0
	
main()