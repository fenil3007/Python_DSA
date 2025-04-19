class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    
    def isempty(self):
        return len(self.items)==0    
    
    def pop(self):
        if self.isempty():
            raise IndexError("Priority Queue is Empty.")
        else:
            return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
    
p = PriorityQueue()
p.push("Fenil",3)
p.push("Meet",1)
p.push("Priyansa",6)

while not p.isempty():
    print(p.pop())
# print(p.size())        
                           