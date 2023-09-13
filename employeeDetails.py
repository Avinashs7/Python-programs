class Employee:
    def __init__(self,name,sal,dept):
        self.name=name
        self.department=dept
        self.salary=sal
    def display(self):
        print("Employee name ",self.name)
        print("Employee department ",self.department)
        print("Employee salary ",self.salary)
    def updateSal(self,sal,dept):
        if(self.department==dept):
            self.salary=sal
n=int(input("Enter number of employees"))
Emp=[]
for i in range(n):
    name=input("Enter employee name\n")
    dept=input("Enter employee's department\n")
    sal=int(input("Enter eployee's salary\n"))
    emp=Employee(name,sal,dept)
    Emp.append(emp)
print("Displaying all employee records")
for i in range(n):
    Emp[i].display()
print(" ")
dept=input("Enter department to update salary")
salary=int(input("Enter updated salary"))
for i in range(n):
    Emp[i].updateSal(sal,dept)
    Emp[i].display()
    
    