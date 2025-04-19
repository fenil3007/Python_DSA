class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def isempty(self):
        return self.front==None
    def insert_front(self,data):
        n =Node(data,None,self.front)
        if self.isempty():
            self.rear=n
        else:
            self.front.prev=n    
        self.front=n 
        self.item_count+=1
    def insert_rear(self,data):
        n=Node(data,self.rear,None)
        if self.isempty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1 
    def delete_front(self):
        if self.isempty():
            raise IndexError("Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1
        
    def delete_rear(self):
        if self.isempty():
            raise IndexError("Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1
    
    def get_front(self):
        if self.isempty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item
    
    def get_rear(self):
        if self.isempty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
d1 = Deque()
d1.insert_front(20)
d1.insert_front(10)
d1.insert_front(0)
d1.insert_rear(30)
d1.insert_rear(40)
d1.delete_front()
d1.delete_rear()

print(d1.get_front())
print(d1.get_rear())          
                            
                            
               
    
    
                   