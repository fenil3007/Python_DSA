#Two types of Objects 
# 1.class Objects - one which is create with the defination of the class itself  ex-class Employee
# 2.instance Objects - which one is created with the class object  ex-e1= Employee()


class Employee: # class object
    def __init__(self,empid=None,name=None,salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary
    def setempid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary
    def getempid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
e1 = Employee() # instance object
e2=Employee(2,"Fenil",20000)
e1.setempid(1)
e1.setName("Meet")
e1.setSalary(50000)
e2.setSalary(30000)
print(e1.getempid(),e1.getName(),e1.getSalary())
print(e2.getempid(),e2.getName(),e2.getSalary())


class Test:
   count = 0
   @staticmethod
   def add(x,y):
       return x+y
   def increment_count(cls):
       cls.count+=1
    
    
    
   
t1=Test()
t1.increment_count()
t1.increment_count()
t1.increment_count()
res = t1.add(22,23)
print("The sum of passing number is:",res)


print(t1.count)