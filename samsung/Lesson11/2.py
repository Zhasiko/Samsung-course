class User:
    def __init__(self,id,login,password,role):
        self.__id = id
        self.__login = login
        self.__password = password
        self.__role = role
        
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
    def role(self):
        return self.__role
    @role.setter
    def id(self, role):
        self.__role = role
        

    def getAllData(self):
        return self.id, self.login, self.password, self.role
    
user1 = User(46,"John","6542564","guest")
user2 = User(5462,"Frank","Sz45265","manager")
user3 = User(45,"Roy","sf454545","boss")
user4 = User(25,"Kil","csd151","guest")
user5 = User(244,"Billy","gf515151","manager")
user6 = User(4564,"Gray","vdf468484","boss")
user7 = User(42,"Hurry","rtv4889498","guest")
user8 = User(78,"Volk","csdf516651","manager")
user9 = User(89,"Shalkar","xcvb654654","boss")
user10 = User(98,"Cisco","cxv8948924","boss")


users = [user1, user2, user3, user4, user5, user6, user7, user8, user9,user10]

log = input("Login: ")
pas = input("Password: ")

for u in users:
    if log == u.login and pas == u.password:
        print("Welcome,",u.login)
        a = input('''
Press 1 to edit login
Press 2 to change password
Press 3 to delete account
Press 0 to exit
''')
        if a == '1':
            u.login = input("new login: ")
        elif a == '2':
            u.password = input("new password: ")
        elif a == '3':
            users.remove(u)
        elif a == '0':
            print("bye")
        print(u.login,u.password)
    else:
        ("Not availabe")
