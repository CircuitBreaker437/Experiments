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
    seasonalEmployeeCount = 0
    
    def __init__(self, nameSeasonal, salarySeasonal):
        #self.employee_count += 1 #in here the global employee_count will not incremented!!!
        Employee.employee_count += 1 #this will incerement the global employee count
        SeasonalEmployee.seasonalEmployeeCount += 1
        self.employee_name = nameSeasonal
        self.employee_salary = salarySeasonal
        

employee4 = SeasonalEmployee('Janek', 13000)


print("Current total count(4): %d" % employee4.employee_count)
print ("Current total count(3): %d" % employee3.getCurrentCount())
print ("Current total seasonal employee count: %d" % employee4.seasonalEmployeeCount)
