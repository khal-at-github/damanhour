from math import *
def binary_search(array,targetValue):
	min = 0
	max = len(array)
	count = 0
	while max>=min:
		guess = floor((max+min)/2)		
		count += 1
		if array[guess]==targetValue:
			return guess
		elif array[guess]<targetValue:
			min=guess+1;
		else:
			max=guess-1
			
	return -1