class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next = next

class StackUsingLinkedList:
    def __init__(self):
        self.start=None
        self.item_count = 0
     
    def isempty(self):
        return self.start== None     
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
        
    def pop(self):
        if not self.isempty():
            data = self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is Empty.")   
            
    def peek(self):
        if not self.isempty():
            return self.start.item
        else:
            raise IndexError("There is no element in the stack.")
    
    def size(self):
        return self.item_count
    
s1=StackUsingLinkedList()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.pop())
print(s1.peek())
print("The size of the stack is: ",s1.size())
         