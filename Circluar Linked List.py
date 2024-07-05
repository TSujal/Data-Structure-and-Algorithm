## The node class here remains same as Singly Linked List
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class CSLinkedList:
    """
    #Creating just one element circlular linked list
    def __init__(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    """
    # No node/empty Circular linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head #pointer to the first node
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    #append method to insert or add a node to the Circular linked list
    def append(self,value):
        new_node = Node(value) #creating a new node
        #if there is no node/ie empty CSLL
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length +=1

    #inseeting the element in the beginning of the CSLL
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next= new_node
        self.length +=1

    #inserting the element in the index position
    def insert(self,index,value):
        new_node = Node(value)

        if index == 0:
            if self.head == None and self.tail == None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    #traversing to the CSLL
    def traverse(self):
        current = self.head
        while current is not None: ## O(n)
            print(current.value)
            current = current.next
            if current == self.head:
                break

    #searching the element in the CSLL
    def search(self,value):
        current = self.head
        while current is not None: ## --> O(n)
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    #get method to input index and return the node value
    def get(self,index):
        current = self.head
        if index < -1 or index >= self.length:
            return None
        for _ in range(index):
            current = current.next
        return current
    #set method to update any given index by the given value
    def set(self,index,value):
        temp = self.get(index)#to find the index value we will use get method
        if temp is not None:
            temp.value = value
            return True
        return False
    #time & space complexity = O(1)

    #POP first method- which is going to take out first node and return its value
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:#edge case
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
            return popped_node
        #the time complexity of this function is constant O(1)

    #pop method which is simply going to pop out the last node value form the CSLL
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.head = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    #the run time and space complexity is constant O(1)

    def remove(self,index):
        temp = self.get(index)
        prev = self.head
        while prev.next is not temp:
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    """
    OR it can be done this way too...given by video
    above one is done by me
    """
    """
    def remove(self,index):
        prev_node = self.get(index-1)
        poped_node = prev_node.next
        prev_node.next = poped_node.next
        poped_node.next = None
        self.length -=1
        return poped_node
    """




cs_linkedlist = CSLinkedList()
print(cs_linkedlist.head)
cs_linkedlist.append(10)
cs_linkedlist.append(20)
cs_linkedlist.append(30)
cs_linkedlist.append(40)
print(cs_linkedlist)
cs_linkedlist.prepend(1)
print(cs_linkedlist)
cs_linkedlist.insert(1,2)
print(cs_linkedlist)
cs_linkedlist.insert(0,0)
print(cs_linkedlist)
cs_linkedlist.insert(7,7)
print(cs_linkedlist)
print(cs_linkedlist.tail.value)
print(cs_linkedlist.traverse())
print("-------------------------------")
print(cs_linkedlist.search(20))

print("-------------------------------")
print(cs_linkedlist.get(3))
print("Performing Set method")
print(cs_linkedlist.set(3,300))
print(cs_linkedlist)
print("Poped  first node value:",cs_linkedlist.pop_first().value)
print(cs_linkedlist)
print("POPED LAST METHOD")
print(cs_linkedlist)
cs_linkedlist.pop()
print(cs_linkedlist)

#Using remove method
cs_linkedlist.remove(2)
print(cs_linkedlist)