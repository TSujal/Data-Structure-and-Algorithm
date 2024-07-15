##Sujal Leet Code Easy
## Implementing Stacks using Queues Leet code problem
class MyStack:
    def __init__(self):
        self.q = queue()
    def push(self, x):
        self.q.append(x)
    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft()) #from left where we will pop
        return self.q.popleft()
    def top(self):
        return self.q[-1]
    def empty(self):
        return len(self.q)==0


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    print("Let's test the pop")
    print(my_stack.pop())