class Student:
    def __init__(self, name, surname, gpa):
        self.name = name
        self.surname = surname
        self.gpa = gpa
        
    def getStudentData(self):
        return f"Name:{self.name}, Surname:{self.surname}, GPA:{self.gpa}"
    
def topStudent(array_of_gpa):
    print(max(array_of_gpa))
        
    
Student1 = Student("Temir","Zholdas",3.78)
Student2 = Student("Erik","Khasen",3.0)
Student3 = Student("Zhandos","Baiken",3.08)
Student4 = Student("Kazi","Ali",3.75)
Student5 = Student("Eskendir","Abay",3.46)
Student6 = Student("sad","Zhoasdldas",3.78)
Student7 = Student("Eradasik","Khsdsasen",3.0)
Student8 = Student("aSD","BaikeAsdn",1.08)
Student9 = Student("asasdd","aasdsd",3.75)
Student10 = Student("aasdsds","sd",3.46)

students = [Student1,Student2,Student3,Student4,Student5]

for student in students:
    print(student.getStudentData())