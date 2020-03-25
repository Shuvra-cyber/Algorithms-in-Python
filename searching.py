#Contents:
#
# 1.Linear Search
# 2.Binary search
# 3.Jump Search
# 4.Interpolation Search
# 5.Exponential Search

from math import *

#Linear search algorithm O(n)

def linear_search(Array,Element):
    i = 0
    for i in range(len(Array)):
        if Element == Array[i]:
            return i
    else:
        return -1

# give sorted array binary search algorithm O(Log n)

def binary_search(Array,Element):
    low_index = 0
    high_index = len(Array)
    
    while high_index >= low_index:
        
        mid = int((low_index + high_index)//2)
        
        if Element == Array[mid]:
            return mid
        elif Element > Array[mid]:
            low_index = mid + 1
        elif Element < Array[mid]:
            high_index = mid - 1
        else:
            return -1
        
#algorithm of jump sort O(n**(1/2))

def jump_search(Array,Target):
    
    jump = int(sqrt(len(Array)))
    jump_step = 0
    
    while Array[jump*jump_step] <= Target and jump*jump_step <= len(Array):
        jump_step += 1
        jumpings = jump*jump_step
        if jumpings > len(Array):
            return -1
    
    jumpings -= jump
    
    for i in range(jumpings,len(Array)):
        if Array[i] == Target:
            return i
    else:
        return -1

# algorithm for interpolation sort
#probe formula position = low_index + ((target - Array[low_index])*(high_index - low_index)/(Array[high_index] - Array[low_index]))

def interpolation_search(Array,Target):
    low_index = 0
    high_index = len(Array) - 1

    position = low_index + ((Target - Array[low_index])*(high_index - low_index)/(Array[high_index] - Array[low_index]))
    while low_index < high_index:
        if Target == Array[position]:
            return position
        elif Target < Array[position]:
            low_index = position + 1
        else:
            high_index = position - 1
    else:
        return -1

#algorithm for exponential search 

def exponential_search(Array,Target):
	i = 0
	start = 2**i
	if len(Array) == 1 and Target != Array[0]:
		return -1

	while Array[start - 1] <= Target:
		i += 1
		start = 2**i

	start = 2**(i-1)

	for j in range(start,len(Array)):
		if Array[j] == Target:
			return j
	else:
		return -1


#print(linear_search(list(range(5,101)),56))	
#print(binary_search(list(range(5,101)),56))
#print(jump_search(list(range(5,101)),56))
#print(interpolation_search(list(range(5,101)),56))
#print(exponential_search(list(range(5,101)),56))
