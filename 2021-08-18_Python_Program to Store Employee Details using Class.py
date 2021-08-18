#Python Program to Store Employee Details using Class
"Computer Programming Tutor, Aug16th,2021"

class staff:
    count = 0
    def __init__(self,name,desig,salary):
        self.name = name
        self.desig = desig
        self.salary = salary
        staff.count +=1

    def displayCount(self):
        print("There are %d Employees" %staff.count)

    def displayDetails(self):
        print("Name:",self.name, "Designation:",self.desig,",Salary[£]:",self.salary)

rec1 = staff("Lijia","Coach", 82000)
rec2 = staff("Ernie","Dreamer",90000)
rec3 = staff("Yijie","Engineer",84000)
rec4 = staff("Shen Fan","Civil Engineer",75000)
rec4.displayCount()

print("Details of All Employees:")
rec1.displayDetails()
rec2.displayDetails()
rec3.displayDetails()
rec4.displayDetails()

