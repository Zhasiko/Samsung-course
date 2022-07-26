#parent class(subclass)

#parent
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return f"{self.name} is working"
    
class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name,age)
        self.group = group
    def work(self):
        return super(Student, self).work()
        
persom = Person("p",20)
st = Student("s",18,1)
print(st.work())