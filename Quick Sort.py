### QUICK SORT ALGORITHM
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() #the pop method takes the last elements from the sequence and assign it to pivot
    items_greater = [] #making a right list
    items_lower = [] #making a left side list
    for items in sequence:
        if items > pivot:
            items_greater.append(items)
        elif items < pivot:
            items_lower.append(items)
    return quick_sort(items_lower) +  [pivot] + quick_sort(items_greater)

#print(quick_sort([6,9,8,1,3,9,0,3,44]))
#quick sort is more prominently used sorting algo because it out performs others
#the time complexity of quick sort is (nlogn)


#Interview questions:
"""
Implement Quick sort in python but use a different pivot selection 
method (eg.., choose the median of the first, middle, and the 
last element as a pivot)
"""
def quick_sort_with_median_pivot(sequence):
    length = len(sequence) #detecting the length of the array
    #lst = []
    if length <= 1:
        return sequence
    else:
        #selecting median as pivot
        first = sequence[0]
        middle = sequence[length//2]
        last = sequence[length-1]
        if (first <= middle <= last) or (last <= middle <= first):
            pivot = middle
        elif (middle <= first <= last) or (last <= first <= middle):
            pivot = first
        else:
            pivot = last
        #print("pivot",pivot)
    #partitions.....
    equal_lst = [] #handling duplicates
    greater_lst = []
    lower_lst = []
    for item in sequence:
        if item > pivot:
            greater_lst.append(item)
            #print("Greater Element:",greater_lst)
        elif item < pivot:
            lower_lst.append(item)
            #print("Lower Element:",lower_lst)
        elif item == pivot:
            equal_lst.append(item)
    return quick_sort_with_median_pivot(lower_lst) + equal_lst + quick_sort_with_median_pivot(greater_lst)

#print(quick_sort_with_median_pivot([1,2,24,24,12,36,72,15,15,67,3]))



## Implementing the Quick sort without recursive
def quick_sort_non_recursive(sequence):
    stack = [(0,len(sequence)-1)]
    #print("stack:",stack) #indices
    while stack:
        start,end = stack.pop()
        #print("start:",start,"end:",end)
        if start >= end:
            continue
        pivot = sequence[start] #initializing the pivot as the first elemtns of the sub-sequences

        left = start + 1 #initializing indices for partitions ie 1
        right = end #ie 4
        while left <= right:
            while left <= right and sequence[left] <= pivot:
                left += 1
            while left <= right and sequence[right] > pivot:
                right -=1
            if left < right:
                sequence[left], sequence[right] = sequence[right], sequence[left] #swapping
                left +=1
                right -=1
        sequence[start], sequence[right] = sequence[right], sequence[start]
        stack.append((start,right-1))
        stack.append((right+1,end))
    return sequence
#print(quick_sort_non_recursive([2,1,3,4,5,6,99,2,4]))



## Random Pivot
import random
def quick_sort_random_pivot(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = random.choice(sequence) #the pop method takes the last elements from the sequence and assign it to pivot
    items_equal = [] #equal items/duplicate
    items_greater = [] #making a right list
    items_lower = [] #making a left side list
    for items in sequence:
        if items > pivot:
            items_greater.append(items)
        elif items < pivot:
            items_lower.append(items)
        else:
            items_equal.append(items)
    return quick_sort_random_pivot(items_lower) +  items_equal + quick_sort_random_pivot(items_greater)
#print("Random pivot Quick sort",quick_sort_random_pivot([3,3,4,2,1,5,9,4,6,7,6]))