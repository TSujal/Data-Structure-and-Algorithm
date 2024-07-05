## Creating the Stack using LIST
# Creating without any size limit
class Stack:
    def __init__(self):
        self.list = [] #creating an empty stack

    def __str__(self):
        #values = self.list.reverse() #its going to take from last element
        values = [str(x) for x in reversed(self.list)] #and then store every thing into a variable
        return '\n'.join(values)#and here in every new line we will have one element last to first

    def isEmpty(self):
        if self.list ==[]:
            return True
        return False
    # Constant time complexity

    def push(self,value):
        self.list.append(value)
        return list

    def peek(self):
        return self.list[-1]

    def pop(self):
        if self.isEmpty():
            return "ITs not possible to pop empty list"
        else:
            return self.list.pop()

    def delete(self):
        self.list = None
        return list

"""
customstack = Stack()
print(customstack.isEmpty())
customstack.push(10)
customstack.push(20)
customstack.push(30)
customstack.push(40)
print(customstack)
print("-----------------------")
print(customstack.pop())
print("-----------------------")
print(customstack)
print("-----------------------")
print(customstack.peek()) #just gives out the last element value here.
"""


### Creating the stack with LIMIT TO size
class Stack_limit:
    def __init__(self,maxSize): #maxSize is the maxSize that stack can have
        self.maxSize = maxSize
        self.list = []


    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    def isEmpty(self):
        if self.list ==[]:
            return True
        return False

    def isFull(self):
        if self.list == self.maxSize: return True
        return False

    def peek(self):
        if self.isEmpty():
            return "Its not possible to"
        return self.list[-1]

    def pop(self):
        if self.isEmpty():
            return "Its not possible to pop empty list"
        return self.list.pop()

    def push(self,value):
        if self.isFull():
            return "Stack is Full, you can't add more elements"
        return self.list.append(value)
"""
customstack = Stack_limit(4)
print(customstack.isEmpty())
customstack.push(10)
customstack.push(20)
customstack.push(30)
customstack.push(40)
print(customstack)
print("-----------------------")
print(customstack.pop())
print("-----------------------")
print(customstack)
print("-----------------------")
print(customstack.peek()) #just gives out the last element value here.

customstack.push(500)
print(customstack)
print("---------------------")
customstack.push(600)
print(customstack)
print("---------------------")
print(customstack.isFull())

"""


### Creating the Stack using the LINKED LIST
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack_Linked_list:
    def __init__(self):
        self.Linked_List = LinkedList() #creating a stack here
    def isEmpty(self):
        if self.Linked_List.head == None:
            return True
        return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.Linked_List.head
        self.Linked_List.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            nodeValue = self.Linked_List.head.value
            self.Linked_List.head = self.Linked_List.head.next
            return nodeValue

        
custom_stack_LL = Stack_Linked_list()
print(custom_stack_LL.isEmpty())
custom_stack_LL.push(10)
custom_stack_LL.push(20)
custom_stack_LL.push(30)
custom_stack_LL.push(40)
print(custom_stack_LL.isEmpty())
print(custom_stack_LL)
