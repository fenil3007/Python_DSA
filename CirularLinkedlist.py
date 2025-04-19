class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last =last
    def isempty(self):
        return self.last is None
    def insert_at_start(self,data):
        n = Node(data)
        if self.isempty():
            n.next = n
            self.last=n
        else:
            n.next = self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n = Node(data)
        if self.isempty():
            n.next = n
            self.last =n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n 
            
    def search(self,data):
        if self.isempty():
            return None
        temp = self.last.next
        while(temp is not self.last):
            if(temp.data==data):
                return temp
            temp=temp.next
        if temp.data==data:
            return temp 
        return None    
            
            
                    
               
    def insert_at_between(self,data,middle_node):
        if middle_node is not None:
            n = Node(data,middle_node.next)
            middle_node.next = n
            if middle_node==self.last:
                self.last=n
    
    def printlist(self):
        if not self.isempty():
            temp = self.last.next
            while(temp is not self.last):
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)
           
    def delete_at_start(self):
        if not self.isempty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next=self.last.next.next
    
    def delete_at_end(self):
        if not self.isempty():
            if self.last.next == self.last:
                self.last=None
            else:       
                temp = self.last.next
                while(temp.next is not self.last):
                    temp = temp.next
                temp.next = self.last.next
                self.last=temp 
        
    def delete_at_between(self,data):
        if not self.isempty():
            if self.last.next == self.last:
                if self.last.data == data:
                    self.last = None
            else:
                if self.last.next.data == data:
                    self.delete_at_start()
                else:                      
                    temp = self.last.next
                    while(temp is not self.last):
                        if temp.next ==  self.last:
                            if self.last.data == data:
                                self.delete_at_end()
                                break
                        if(temp.next.data==data):
                            temp.next= temp.next.next
                            break
                        temp = temp.next
                        
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)                    
                        
class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.first=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.first and self.count==0:
            raise StopIteration
        else:
            self.count=1
        data=self.current.data
        self.current=self.current.next
        return data   
    
    
    
cll=CLL()
cll.insert_at_start(10)
cll.insert_at_last(20)
cll.insert_at_last(40)
cll.insert_at_between(30,cll.search(20))
# cll.printlist()
for i in cll:
    print(i,end=" ")    
            
        
                          
                        
                        
                            
                                
                       
                        
                             
             
                         
                                    