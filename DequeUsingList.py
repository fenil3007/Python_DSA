class Deque:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.isempty():
            raise IndexError("Deque is Empty.")
        else:
            self.items.pop(0)
    def delete_last(self):
        if self.isempty():
            raise IndexError("Deque is Empty.")
        else:
            self.items.pop()
    def get_front(self):
        if self.isempty():
            raise IndexError("Deque is Empty.")
        else:
            return self.items[0]   
    def get_rear(self):
        if self.isempty():
            raise IndexError("Deque is Empty.")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)  
    
d1 = Deque()
d1.insert_front(10)
d1.insert_front(5)
d1.insert_front(0)
d1.insert_rear(15)
d1.insert_rear(20)
d1.delete_front()
print(d1.get_front())
print(d1.get_rear())
print(d1.items)           
                     
        
    