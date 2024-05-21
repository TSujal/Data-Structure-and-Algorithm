"""
Interview Question: given a sorted array of integers, write a function to search for a specific target value and
return its index. if the target is not found, return -1
"""

def binary_search(array, target):
    """
    Performs binary search to find the target value in the sorted array
    :param
        array: A sorted list of array of integers
        target: The integer value to search for in the array
    :return:
        The index of the target value in the array, or -1
        if the target is not found
    """
    #initialize the pointers for binary search
    left = 0  #let's assume 5 items ie left = 0 as position/index
    right = len(array) - 1 #this is 4
    while left <= right:
        mid = left + (right - left) // 2 #mid point ie 2 ie 3rd value in the array
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    #if target is not found
    return -1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 66
    print(f"Experiment 1: Index of {target} is : {binary_search(array, target)}")
    target_1 = 5
    print(f"Experiment 1: Index of {target_1} is : {binary_search(array, target_1)}")


"""
Question:
Given a sorted array of integers and a target value, write a function to find the index 
of the smallest element in the array that is greater than or equal to the target value.
If no such element exists, return -1.

Eg: array = [1,2,5,6,8,9,13,16,17,20]
target = 10
"""

def find_lower_bound(array, target):
    """
    Find the index of the smallest elements in the array that is
    greater then or equal to target
    :param array: A sorted array of integers
    :param target: interger value to search for....
    :return:
    The index of the smallest element >= target or -1 if target is not found
    """
    left = 0 #assume len = 5 starting with 0th position index
    right = len(array) - 1 # 4
    result = -1 #if not found the items in or target
    while left <= right:
        mid = left + (right-left) // 2

        if array[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

if __name__ == "__main__":
    array = [1,2,5,6,8,9,13,16,17]
    target = 3
    print(f"Index for lower bound is : {find_lower_bound(array,target)}")
    print(f"ie the value : {array[find_lower_bound(array,target)]}")