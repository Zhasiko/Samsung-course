from ipaddress import ip_address


class User:
    def __init__(self, id, login, password, name, surname):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login):
        self.__login = login
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        

    def getAllData(self):
        return self.id, self.login, self.password, self.name,self.surname
        
class Staff(User):
    def __init__(self, id, login, password, name, surname,salary, subjects):
        super().__init__(id, login, password, name, surname)
        self.salary = salary
        self.subjects = subjects
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login):
        self.__login = login
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        
    @property
    def subjects(self):
        return self.__subjects
    @subjects.setter
    def subjects(self, subjects):
        self.__subjects = subjects
        
    def getAllData(self):
        return super().getAllData(), self.salary, self.subjects
    
    
        
class Student(User):
    def __init__(self, id, login, password, name, surname,gpa, courses):
        super().__init__(id, login, password, name, surname)
        self.gpa = gpa
        self.courses = courses
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login):
        self.__login = login
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa
        
    @property
    def courses(self):
        return self.__courses
    @courses.setter
    def courses(self, courses):
        self.__courses = courses
        
    def getAllData(self):
        return super().getAllData(), self.gpa, self.courses
        
user = User(1,'Zhasik',"123456","Zhassulan","Issayev")
student1 = Student(2,"JNY","7892","John","New",4.0,['math','physics'])
staff1 = Staff(3,'yut',"lkjh55","Phil","johns",5000,['math'])

students = [student1]
staffs = [staff1]

a = input('''
Press 1 to add user
Press 2 to list users
Press 0 to exit
''')

if a == '1':
    b = input('''
Press 1 to add Student
Press 2 to add Staff
''')
    if b == '1':
        id = int(input("id: "))
        login = input("login: ")
        password = input("password: ")
        name = input("name: ")
        surname = input('surname: ')
        gpa = float(input("gpa: "))
        courses = input("courses: ").split()
        students.append(Student(id,login,password,name,surname,gpa,courses))
    if b == '2':
        id = int(input("id: "))
        login = input("login: ")
        password = input("password: ")
        name = input("name: ")
        surname = input('surname: ')
        salary = int(input("salary: "))
        subjects = input("subjects: ").split()
        students.append(Staff(id,login,password,name,surname,salary,subjects))
        
        
    
if a == '2':
    b = input('''
Press 1 to list Students
Press 2 to list Staff
''')
    if b == '1':
        for i in students:
            print(i.name)
    if b == '2':
        for i in staffs:
            print(i.name)
    
if a == '0':
    exit()