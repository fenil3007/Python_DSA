class Stack:
    def __init__(self):
        self.items = []
    
    def isempty(self):
        return len(self.items) == 0
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.isempty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.isempty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.items)
    

s1 = Stack()
s1.push(20)
s1.push(23)
s1.push(25)
print(s1.peek())
s1.pop()
s1.pop()
s1.pop()


print(s1.items)