class StackUsingInheritingList(list):
    def isempty(self):
        return len(self) == 0
    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.isempty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self):
        if not self.isempty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty.")
        
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No Attribute: 'insert' in stack")
    
s1 = StackUsingInheritingList()
s1.insert(1,24)
print(s1)