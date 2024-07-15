
## Sujal Leet-Code problem [Easy]
## implementing Queues using 2 Stack
class MyQueue():
    def __init__(self):
        self.s1 = [] #stack1
        self.s2 = [] #stack2
    def push(self,x:int):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1),len(self.s2)) == 0



