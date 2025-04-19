class Node:
    def __init__(self,item=None,next=None,previous=None):
        self.item=item
        self.next=next
        self.previous=previous
class DLL:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start is None
    def printlist(self):
        current=self.start
        while current is not None:
            print(current.item,end=" ")  
            current=current.next
    
    def insert_At_Begin(self,data):
        n  = Node(data,self.start)
        if not self.isempty():
            self.start.previous = n
        self.start=n
        
     
    def insert_At_Last(self,data):
             
        current =self.start
        if self.start!=None:           
            while current.next!=None:
                current = current.next
        n = Node(data,None,current)  
        if current==None:
            self.start =n
        else:
            current.next=n    
        
    def insert_At_Between(self,middle_node,data):
        
        if middle_node is not None:
            n=Node(data,middle_node.next,middle_node)
            if middle_node.next is not None:
                middle_node.next.previous=n
            middle_node.next=n    
    
    def delete_from_begin(self):
        if not self.isempty():
            self.start=self.start.next 
            if self.start is not None:
                self.start.previous = None 
      
    def delete_from_last(self):
        if not self.isempty():
            if self.start.next is None:
                self.start=None
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.previous.next = None
                
    def delete_from_between(self,data):
        if self.start is None:
            pass
        else:
            temp= self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.previous=temp.previous
                    if temp.previous is not None:
                        temp.previous.next=temp.next
                    else:
                        self.start= temp.next
                    break            
                temp = temp.next
                    
    def search(self,data):
        temp =self.start
        while(temp.next):
            if temp.item==data:
                return temp
            temp = temp.next 
        return None    
            
             
    def __iter__(self): 
        return DLLIterator(self.start)        
            
                         
                                      
                       
class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data                    
    
    
dll=DLL()
dll.start=Node("fenil",None,None)
n1 = Node("kalp",None,dll.start)
n2=Node("purvish",None,n1)
n3=Node("hemanshu",None,n2)
dll.start.next=n1
n1.next=n2
n2.next=n3

dll.insert_At_Begin("Mohit")
dll.insert_At_Begin("Denish")
dll.insert_At_Begin("Akash")
dll.insert_At_Last("Akash")
dll.insert_At_Last("Pinak")
dll.insert_At_Last("Aryan")
dll.insert_At_Between(n2,"Tithi")
dll.delete_from_begin()
dll.delete_from_last()
dll.delete_from_between("fenil")

# for i in dll:
#     print(i,end=" ")
dll.printlist()







