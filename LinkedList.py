class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
        
    def isempty(self):
        return self.start is None
    
    def printlist(self):
        current = self.start
        while current is not None:
            print(current.item,end=" , ")
            current=current.next
            
    def insert_At_begin(self,newdata):
        NewNode = Node(newdata,self.start)
        self.start= NewNode
    
    def insert_At_last(self,newdata):
        NewNode = Node(newdata)
        if not self.isempty():
            laste=self.start
            while(laste.next):
                laste=laste.next
            laste.next=NewNode
        else:
            self.start=NewNode
    
    def search(self,data):
        temp = self.start
        while(temp.next is not None):
            if temp.item == data:
                return temp 
            temp = temp.next 
        
    def insert_At_between(self,middle_node,newdata):
       
        if middle_node is not None:
             NewNode=Node(newdata,middle_node.next)
             middle_node.next = NewNode
        
    def delete_from_start(self):
        if not self.isempty():
            self.start=self.start.next
        
    def delete_from_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    
    
    def delete_from_between(self,data):
        if self.start  is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
        
    def __iter__(self):
        return SLLIterator(self.start)
        
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):   
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current = self.current.next  
        return data
         
        
sll = SLL()
sll.start=Node("First")
n1=Node("Second")
n2=Node("Third")
sll.start.next = n1
n1.next=n2
sll.insert_At_begin("Added at first")
sll.insert_At_last("Added to the last")
sll.insert_At_between(n1,"Added after n1 node")
sll.printlist()
sll.delete_from_between('Second')
sll.delete_from_end()
sll.delete_from_end()
print("\n")
for i in sll:
    print(i,end=" ")
