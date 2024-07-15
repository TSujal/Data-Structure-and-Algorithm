## done by Sujal thakkar
## implementing Stack using Singly Linked List

class SLLStack:
    class Node:
        def __init__(self,element,_next):
            self.element = element
            self._next = _next
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def push(self,element):
        self.head = self.Node(element,self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty currently")
        result = self.head.element #returns the head
        self.head = self.head._next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        return self.head.element


if __name__ == "__main__":
    s = SLLStack()
    s.push(1)
    print("check the size:",len(s))
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print("check the size:",len(s))
    print("Check what's on the top of the stack :", s.top())
    #print("Check what's pop's up when you pop first element:",s.pop())
    while not s.is_empty():
        print(f"Element popped: {s.pop()}")