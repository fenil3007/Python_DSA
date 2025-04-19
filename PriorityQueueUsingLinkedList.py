class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
        
class Priority:
    def __init__(self):
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp = self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1    
            
    def isempty(self):
        return self.start==None       
    
    def pop(self):
        if self.isempty():
            raise IndexError("Priority Queue is Empty")
        else:
            data = self.start.item
            self.start= self.start.next
            return data  
        self.item_count-=1
    
    def size(self):
        return self.item_count
  
p = Priority()
p.push("Fenil",3)
p.push("Meet",1)
p.push("Priyansa",6)

while not p.isempty():
    print(p.pop())
                            