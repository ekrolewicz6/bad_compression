# Create a binary file of length n
import random
import sys
from time import time
from get_size import total_size

def generateBinary(length, string):
	# Generates all permutations of binary strings of lengh n
	if(length > 0):
	    generateBinary(length-1, string + "0")
	    generateBinary(length-1, string + "1")
	else:
	    bidict[string] = []

def encode(file, window_length):
	# check hash and add the iteration to hashtable
	i = 0
	while len(file) != 0:
		part = file[:window_length]
		file = file[window_length:]
		if part in bidict:
			bidict[part].append(i)
			# print("Iteration %d. Appended %s to bidict" % (i,part))
		else:
			bidict["end"] = part
			print("And this is the end part: %s" % part)
		i += 1

def decode(bidict, file, window_length):
	size = int(len(file)/window_length)
	# print(size)
	if len(file)%window_length !=0:
		size+=1
	a = [0] * size # create an array of size N/10 to store all the iterations in the binary dictionary.
	# go through each key on bidict and add all the keys values to the corresponding index value in n
	for key in bidict:
		if key == 'end':
			a[-1] = bidict[key]
		elif len(bidict[key]) is not 0: #if the array has anything in it
			for i in bidict[key]:
				a[i] = key #add the key to that part of the array
	return "".join([x for x in a])

def generateBinaryNumber(length):
	s = ""
	while length != 0:
		s += str(random.choice([0,1]))
		length -= 1
	return s

# Main
t0 = time()
file = generateBinaryNumber(100000) #8,000,000 is one MB
t1 = time()
# Create a binary dictionary of all values 2^10
bidict = {}
file_size = total_size(file)
print("Init Size of File in bytes: %d" %file_size)
for window_length in range(4,10):
	bidict = {}
	generateBinary(window_length,"")
	encode(file, window_length)
	decoded = decode(bidict,file, window_length)
	bidict_size = total_size(bidict)
	# print("Init Size of File in bytes: %d" %file_size)
	# print("Init Size of bidict in bytes: %d" %bidict_size)
	print("Window Length: %d" % window_length)
	print("Compressed item ratio: %r" % (float(bidict_size/file_size)))

# window_length = 10 #the size of the window we will use to cut off binary strings
# t2 = time()
# generateBinary(window_length,"")
# t3 = time() #time to create binary codes
# encode(file, window_length)
# # print(bidict)
# t4 = time() #time to encode
# decoded = decode(bidict,file, window_length)
# t5 = time() #time to decode
# # file_size = len(file)
# file_size = sys.getsizeof(file)
# bidict_size = total_size(bidict)
# print("Init Size of File in bytes: %d" %file_size)
# print("Init Size of bidict in bytes: %d" %bidict_size)
# print("Compressed item ratio: %r" % (float(bidict_size/file_size)))
# print("Length of binary dict: %d entries" % len(bidict))
# print("Binary Number Generated in: %f seconds" %(t3-t2))
# print("Encoded in %f seconds" %(t4-t3))
# print("Decoded in %f seconds" %(t5-t4))
# print("Decoded File Matches original?: %r" %(file==decoded))

# This grows too quickly the larger the file size is, so you need to break up the problem into sbparts.
# For isntance it is much faster to compute this 100 time for a 100,000 bit string, than for a 10,000,000
# bit string.Theoretically you can compress 10Mb (1.25 MB) string in 1 second using this method.

# We only save storage when the symbol we replace the binary number with (in this case
# the iteration number) costs less to send than the 10 digit binary file.
# for example, 1 MB = 8,000,000 and there will be 8,000,000/10 iterations
# meaning 800,000 iterations. By the last iteration we will be sending over a bits 
# once we get past 10 digit long iterations, (or N bits/10)

# We need to figure out how to decode this hashmap in order of
# iteration to recreate the original file.

# 

# You can store the each list of iterations as a node within a B-Tree, 
# sorting by the lowest number, and when that number is removed from the list it will then sort again
# by. the next lowest number, that way we can continue to retrieve and then retrieve them.
