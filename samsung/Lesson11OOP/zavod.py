from cmath import cos
from enum import Enum

class Employee:
    def __init__(self,name,role,department,salary,year):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary
        self.year = year
        
class Car:
    def __init__(self,model,cost,type,year):
        self.model = model
        self.cost = cost
        self.type = type
        self.year = year
        

class Department:
    def __init__(self,name,employeeNum):
        self.name = name
        self.employeeNum = employeeNum

class Role(Enum):
    Admin = 2
    Director = 1
    worker = 3
    
class TypeCar(Enum):
    hatchback = 1
    miniven = 2
    sedan = 3
    cabriolet = 4

class Company:
    def __init__(self, name, departmentNum, carNum):
        self.name = name
        self.departmentNum = departmentNum
        self.carNum = carNum
        
    def generalCostOfCars(self):
        cost = 0
        for i in self.carNum:
            cost += i.cost
        return cost
    
    def avarageOfSalary(self):
        salarygen = 0
        cnt = 0
        for i in self.departmentNum:
            for j in i.employeeNum:
                salarygen += j.salary
                cnt += 1
                
        return salarygen / cnt
    
    def ratingOfCars(self):
        genCost = []
        
        for i in self.carNum:
            genCost.append(i.cost)
                
        return max(genCost), min(genCost)
    
    def staj(self):
        for i in self.departmentNum:
            for j in i.employeeNum:
                if j.year > 5:
                    print(j.name,"get premia")
                    
    def perevod(self, fromDep, ToDep, ind):
        fromDep.pop(ind)
        ToDep.append(ind)
        
        
        
company = Company('Shevrolet', [],[])

department1 = Department('Mechanic',[])
department2 = Department('Accounting',[])
department3 = Department('IT',[])

#Directors
employee1 = Employee('John', Role.Director, department1,5000,5)
employee2 = Employee('Kris',Role.Director,department2,3000,3)
employee3 = Employee('Phil',Role.Director, department3,2900,4)

#Admins
employee4 = Employee('Bale', Role.Admin, department1, 6000, 8)
employee5 = Employee('Margaret',Role.Admin,department2,2546,6)
employee6 = Employee('Kyle',Role.Admin,department3,5446,6)

#Employees
employee7 = Employee('Kim', Role.worker, department1,544,1)
employee8 = Employee('Paul',Role.worker,department2,3442,3)
employee9 = Employee('Eric',Role.worker, department3,4554,4)
employee10 = Employee('Toth', Role.worker, department1, 4154, 4)
employee11 = Employee('Jax',Role.worker,department2,4551,5)
employee12 = Employee('Viera',Role.worker,department3,1234,2)

car1 = Car('Cobalt',2000,TypeCar.hatchback,2022)
car2 = Car('Nexia',1500,TypeCar.hatchback,2019)
car3 = Car('Forester',5600,TypeCar.miniven,2005)
car4 = Car('Optima',4451,TypeCar.cabriolet,2017)
car5 = Car('Cobalt',1550,TypeCar.hatchback,2020)

company.carNum.append(car1)
company.carNum.append(car2)
company.carNum.append(car3)
company.carNum.append(car4)
company.carNum.append(car5)

company.departmentNum.append(department1)
company.departmentNum.append(department2)
company.departmentNum.append(department3)

department1.employeeNum.append(employee1)
department1.employeeNum.append(employee4)
department1.employeeNum.append(employee7)
department1.employeeNum.append(employee10)

department2.employeeNum.append(employee2)
department2.employeeNum.append(employee5)
department2.employeeNum.append(employee8)
department2.employeeNum.append(employee11)

department3.employeeNum.append(employee3)
department3.employeeNum.append(employee6)
department3.employeeNum.append(employee9)
department3.employeeNum.append(employee12)


print(company.generalCostOfCars())
print(company.avarageOfSalary())
print(company.staj())
print(company.ratingOfCars())