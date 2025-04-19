class Node:
    def __init__(self,item=None,next=None):
        self.item=  item
        self.next = next
        




class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def isempty(self):
        return self.item_count == 0
    def enqueue(self,data):
        n=Node(data)
        if self.isempty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+=1
    def dequeue(self):
        if self.isempty():
            raise IndexError("No such element to delete in this queue.")
        elif self.front==self.rear:
            self.front = None
            self.rear = None
            self.item_count-=1
        else:
            self.front = self.front.next
            self.item_count-=1
            
    def getFront(self):
        if self.isempty():
            raise IndexError("Nothing in the queue.")
        else:
            return self.front.item
    def getRear(self):
        if self.isempty():
            raise IndexError("Nothing in the queue.")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
    
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(4)
q1.enqueue(3)
q1.dequeue()
print(q1.getFront()) 
print(q1.getRear())  
        