#creating a Circular Doubly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None 
    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    """
    def __init__(self,value):
        new_node = Node(value)#creating a new node
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    """
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            current = current.next
            if current == self.head: break
            result += " <-> "
        return result

    #append method used to append the new node to the end of the CDLL
    def append(self,value):
        new_node = Node(value) #creating a new Node value
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = self.head
            self.head.prev = new_node
        self.length += 1
    #the run time comlexity  for append method is O(1) constant


    #prepend method
    #which used to add the new node to the beginning of the CDLL
    def prepend(self,value):
        new_node = Node(value) #creating a new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    ## The time complexity of the above method is constant.


    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:break

    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.tail:break
    #the time complexity of this method is O(n)

    def search(self,value):
        temp = self.head
        while temp.value:
            if temp.value==value:
                return True
            temp = temp.next
            if temp == self.head:break
        return False

    def get(self,index):
        len = self.length // 2
        if index < len:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    #the run time of this code is linear as only one loop is here.


    #This method used to setup a new node at the given index
    def set(self,index,value):
        temp = self.get(index) #thus we are pointing to the given index
        if temp is not None:
            temp.value = value
            return True
        return False
    #Constant time complexity

    #insert method is used to insert any new node at any index position
    def insert(self,index,value):
        new_node = Node(value)
        prev = self.get(index-1) #pointing prev node to which we want to change the reference
        #next = self.get(index) #pointing to next node
        new_node.next = prev.next
        new_node.prev = prev
        prev.next = new_node
        prev.next.prev = new_node
        #the run time of this method is O(1) constant

    def pop_first(self):
        if self.head is None: None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        popped.next = None
        popped.prev = None
        self.length -=1
        return popped
    #run time of this code is O(1) constant

    def pop_last(self):
        if self.head ==0: None
        popped = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            #popped = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        popped.prev = None
        popped.next = None
        self.length -=1
        return popped
    #run time of this method is O(1)





print("Creating a CDLL")
CDLL = CircularDoublyLinkedList()#creating a circular DLL
#print("Head value :",CDLL.head.value)
#print("tail value : ",CDLL.tail.value)
#print("Length :",CDLL.length)
print("---------------------------------------")
print("Appending an element",CDLL.append(10))
print(CDLL.append(20))
print(CDLL.append(30))
print("head value before using __str__ constructor:",CDLL.head.value)
print("tail value before using __str__ constructor:",CDLL.tail.value)
print(CDLL)
print("----------------------------------")
print("Implementing Prepend method")
print(CDLL)
CDLL.prepend(1)
print(CDLL)
print("------------------------------------")
print("Implementing Traverse:")
CDLL.traverse()
print("Implementing Reverse Traverse:")
CDLL.reverse_traverse()
print("Implementing Search...")
print(CDLL.search(30))

print("----------------------------------------")
print("Implementing Insert Method")
print(CDLL)
CDLL.insert(2,200)
print(CDLL)

print("----------------------------------------")
print("Implementing POPPED FIRST Method")
print(CDLL)
CDLL.pop_first()
print(CDLL)
print("----------------------------------")
print("Implementing POPPED LAST Method")
print(CDLL)
CDLL.pop_last()
print(CDLL)
