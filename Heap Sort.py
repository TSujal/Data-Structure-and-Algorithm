def swap(lst, i, j):
    """
    Swap the elements by comparing both parent node and child nodes
    :param lst: its the given list
    :param i: loop1
    :param j: loop2
    """
    lst[i], lst[j] = lst[j], lst[i]  # Just swaps

def shift_down(lst, i, upper):
    """
    Shift the elements by comparing both parent node and child in downward direction
    :param lst:
    :param i:
    :param upper:
    :return:
    """
    while True:
        left, right = i * 2 + 1, i * 2 + 2
        # i represents the root node in the beginning
        # i*2+1 is the left children and i*2+2 is the right child of the root node
        if max(left, right) < upper:
            # this means that we do have 2 children for our parent node
            if lst[i] >= max(lst[left], lst[right]):
                break
            # if the parent is greater then left and right child then break
            elif lst[left] >= lst[right]:
                # if the parent node is not greater then child
                # and left child is greater then right then swap
                swap(lst, i, left)
                i = left
            else:
                swap(lst, i, right)
                i = right
        elif left < upper:
            # having only left child
            if lst[left] > lst[i]:
                swap(lst, i, left)
                i = left
            else:
                break
        elif right < upper:
            if lst[right] > lst[i]:
                swap(lst, i, right)
                i = right
            else:
                break
        else:
            # no child
            break

def heapsort(lst):
    """
    Heap sort algorithm
    :param lst: given list
    :return: sorted list
    """
    # step 1: heapify
    # step 2: sort the heapified array/tree
    for j in range((len(lst) - 2) // 2, -1, -1):
        shift_down(lst, j, len(lst))
    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        shift_down(lst, 0, end)

if __name__ == '__main__':
    lst = [5, 16, 8, 14, 20, 1, 26]
    print("original list:",lst)
    heapsort(lst)
    print("Sorted list",lst)


#using Recursion
def max_heapify(arr,n,i):
    largest = i #point to root element
    left =  2*i+1
    right = 2*i+2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,n,largest)

arr=  [2,15,4,30,18,6,25]
n = len(arr)
#build a max heap
for i in range(n//2 - 1 , -1, -1):
    max_heapify(arr,n,i)
#display
print("Max Heap is:")
for i in range(n):
    print(arr[i])




