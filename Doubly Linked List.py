class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
            #f"{self.prev} <- {self.value} -> {self.next}"

#nw_node = Node(10)
#print(nw_node)
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " <-> "
            temp_node = temp_node.next
        return result
    #append method inside the DOubly linked list
    def append(self,value):
        new_node = Node(value) #creating a node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            #new_node.next = None #this things is already None when we create a node its none for both prev and next
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    #time complexity is O(1)

    #prepend to insert element at beginningg of the DLL
    def prepend(self,value):
        new_node = Node(value) #creating a Node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    #the time complexity of this is constant..

    #method to traverse the Doubly linked list
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
    def reverse_traverse(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev

    def search(self,target):
        temp_node = self.head
        while temp_node:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
        return False
    #this method time complexity is O(n) ie linear


    #get method to put the index and get its value
    #here we are going to divide the DLL into half and nearest loc we will pick head or tail
    def get(self,index):
        if index < self.length //2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length-1,index,-1):
                temp_node = temp_node.prev
        return temp_node
    #the run time of this method is O(n) linear because of for loop




    def set(self,index,value):
        if index < self.length//2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.value = value
        else:
            temp_node = self.tail
            for _ in range(self.length-1,index,-1):
                temp_node = temp_node.prev
            temp_node.value = value
        return temp_node
        #Thus the run time of this method is linear again because of one loop
    """
    OR Can also be done this way based on given shown video
    """
    """
    def set_value(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    """

DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(20)
DLL.append(30)
print(DLL)
DLL.prepend(0)
print(DLL)
print("traverse DLL")
DLL.traverse()
print("reverse_traverse")
DLL.reverse_traverse()
print(DLL.search(30))

print("Get method")
print(DLL)
print(DLL.get(2))
print("Working of set method")
print(DLL)
DLL.set(0,1)
print(DLL)

