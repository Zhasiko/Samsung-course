class User:
    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password
        
    def getUserData(self):
        return self.id,self.login, self.password
    
class Student(User):
    def __init__(self, id, login, password, name, surname, group, gpa):
        super().__init__(id, login, password)
        self.name = name
        self.surname = surname
        self.group = group
        self.gpa = gpa

    def getUserData(self):
        return super().getUserData(), self.name, self.surname, self.group, self.gpa
    
class Teacher(User):
    def __init__(self, id, login, password, nick, status,subjects):
        super().__init__(id, login, password)
        self.nick = nick
        self.status = status
        self.subjects = subjects
        
    def addSubject(self,n):
        self.subjects.append(n)
        
    def getUserData(self):
        return super().getUserData(), self.nick, self.status,self.subjects

    