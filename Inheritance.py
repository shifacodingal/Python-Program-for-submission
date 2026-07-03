class person:
    def __init__(self, name, idNumber):
        self.name = name
        self.idNumber = idNumber
        
    def Display(self):
        print(self.name)
        print(self.idNumber)

class Employee(person):
    def __init__(self, name, idNumber, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self,name, idNumber)

ob = Employee("shifa", "EMP1001", 20000, "Tutor")
ob.Display()