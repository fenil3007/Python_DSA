class QueueUsingList:
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        if not self.isempty():
            return self.items.pop()
        else:
            raise IndexError("Queue is somehow empty")
    def front(self):
        if not self.isempty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    def rear(self):
        if not self.isempty():
            return self.items[0]
        else:
            raise IndexError("Again somehow Queue is empty")
q = QueueUsingList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(50)
q.enqueue(100)
q.dequeue()
print(q.items)
print(q.front())
print(q.rear())