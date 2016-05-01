
class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        Employee.employee_count += 1
        self.employee_name = name
        self.employee_salary = salary

    def getCurrentCount(self):
        return(Employee.employee_count)

    def setEmployeeName(self, nameSet):
        self.employee_name = nameSet

    def setEmployeeSalary(self, salarySet):
        self.employee_salary = salarySet

    def __del__(self):
        Employee.employee_count -= 1
        

employee1 = Employee('Marcin', 67000)
employee2 = Employee('Jack', 10000)
employee3 = Employee('Morty', 20000)

print ("Current count(1): %d" % employee1.getCurrentCount())
print ("Current count(2): %d" % employee2.getCurrentCount())
print ("Current count(3): %d" % employee3.getCurrentCount())

del employee2

print ("Current count(1): %d" % employee1.getCurrentCount())
#print ("Current count(2): %d" % employee2.getCurrentCount())
print ("Current count(3): %d" % employee3.getCurrentCount())

class SeasonalEmployee(Employee):
    def __init__(self):
        Employee.employee_count += 1

employee4 = SeasonalEmployee().setEmployeeName('Janek')
employee4 = SeasonalEmployee().setEmployeeSalary(13000)

print("Current count(4): %d" % employee4.getCurrentCount())
