class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
        
    def isempty(self):
        return self.start is None  
    
    def print_list(self):
        if not self.isempty():
            temp=self.start
            while(temp.next is not self.start):
                print(temp.data,end=' ')
                temp=temp.next
            print(temp.data) 
        
            
    def search(self,data):
        temp = self.start
        if temp == None:
            return None
        if temp.data == data:
            return temp
        else:
            temp = temp.next
        
        while temp != self.start:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
                
    def insert_at_begin(self,data):
        n=Node(data)
        if self.isempty():
            n.prev=n
            n.next=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n   
        self.start=n
            
    def insert_at_last(self,data):
        n=Node(data)
        if self.isempty():
            n.prev=n
            n.next=n
            self.start=n
        else:
            n.next = self.start
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev=n                
    
    def insert_between(self,data,middle_node):
        if  middle_node is not None:
            n=Node(data,middle_node,middle_node.next)
            middle_node.next.prev=n
            middle_node.next=n
            
    def delete_from_begin(self):
        if not self.isempty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
            
    def delete_from_end(self):
        if not self.isempty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev=self.start.prev.prev 
                self.start.prev.next=self.start
                
    def delete_node(self,data):
        if not self.isempty():
                temp = self.start
                if temp.data == data:
                    self.delete_from_begin()
                else:
                    temp =temp.next
                    while(temp is not self.start):
                        if temp.data==data:
                            temp.next.prev=temp.prev
                            temp.prev.next=temp.next 
    def __iter__(self):
        return CDLLIterator(self.start)
                                                                        
class CDLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data = self.current.data
        self.current = self.current.next
        return data
            
                

cdll = CDLL()
cdll.insert_at_begin(20)
cdll.insert_at_begin(30)
cdll.insert_at_last(40)
cdll.insert_at_last(20)
# cdll.delete_from_begin()
# cdll.delete_from_end()
cdll.delete_node(cdll.search(30).data)
# cdll.print_list() 
# print(cdll.search(30))  
for i in cdll:
    print(i,end=' ')   