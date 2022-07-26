# объявление класса Мяч
class Ball:
    # конструктор - для инициализации нового объекта
    def __init__(self, diameter, weight):
        self.diameter = diameter
        self.weight = weight

    def printData(self):
        return f"Diameter: {self.diameter}\nWeight: {self.weight}"


class Airplane:

    def __init__(self, name, length, pass_number, max_km):
        self.name = name
        self.length = length
        self.pass_num = pass_number
        self.max_km = max_km

    def fly(self, km):
        return self.max_km > km

    def __str__(self):
        return f"Name: {self.name}, max_km: {self.max_km}"


airplane1 = Airplane("boing8", 120, 320, 320)
airplane2 = Airplane("boing7", 100, 320, 200)
airplane3 = Airplane("boing3", 200, 320, 500)
airplane4 = Airplane("boing81", 130, 320, 240)
airplane5 = Airplane("boing80", 70, 320, 100)

airplanes = [airplane1, airplane2, airplane3, airplane4, airplane5]
# filter()
sorted_airplanes = filter(lambda x: x.max_km > 200, airplanes)
for i in sorted_airplanes:
    print(i)

# if airplane1.fly(200):
#     print("Самолет может лететь")
# else:
#     print("Самолет не может лететь")

# объявление класса Мяч
class Ball:
    # конструктор - для инициализации нового объекта
    def __init__(self, diameter, weight):
        self.diameter = diameter
        self.weight = weight

    def printData(self):
        return f"Diameter: {self.diameter}\nWeight: {self.weight}"


class Airplane:

    def __init__(self, name, length, pass_number, max_km):
        self.name = name
        self.length = length
        self.pass_num = pass_number
        self.max_km = max_km

    def fly(self, km):
        return self.max_km > km

    def __str__(self):
        return f"Name: {self.name}, max_km: {self.max_km}"

# username, password, age
# login, logout, changePassword, encryptPassword
class User:

    def __init__(self, username, password, age):
        self.name = username
        self.password = self.encryptPassword(password)
        self.age = age

    def login(self, username, password):
        return self.name == username and self.password == self.encryptPassword(password)

    def logout(self):
        return "bye bye"

    def encryptPassword(self, password):
        return password[::-1] + "apple"[::-1]
    # qwerty_77_ERLAN

user = User("admin", "qwerty", 22)
print(user.logout())

from operator import attrgetter
# объявление класса Мяч
class Ball:
    # конструктор - для инициализации нового объекта
    def __init__(self, diameter, weight):
        self.diameter = diameter
        self.weight = weight

    def printData(self):
        return f"Diameter: {self.diameter}\nWeight: {self.weight}"


class Airplane:

    def __init__(self, name, length, pass_number, max_km):
        self.name = name
        self.length = length
        self.pass_num = pass_number
        self.max_km = max_km

    def fly(self, km):
        return self.max_km > km

    def __str__(self):
        return f"Name: {self.name}, max_km: {self.max_km}"

# username, password, age
# login, logout, changePassword, encryptPassword
class User:

    def __init__(self, username, password, age):
        self.name = username
        self.password = self.encryptPassword(password)
        self.age = age

    def login(self, username, password):
        return self.name == username and self.password == self.encryptPassword(password)

    def logout(self):
        return "bye bye"

    def encryptPassword(self, password):
        return password[::-1] + "apple"[::-1]
    # qwerty_77_ERLAN



airplane1 = Airplane("boing8", 120, 320, 320)
airplane2 = Airplane("boing7", 100, 320, 200)
airplane3 = Airplane("boing3", 200, 320, 500)
airplane4 = Airplane("boing81", 130, 320, 240)
airplane5 = Airplane("boing80", 70, 320, 100)

airplanes = [airplane1, airplane2, airplane3, airplane4, airplane5]

sorted_airplanes = sorted(airplanes, key=attrgetter("max_km"))

for i in sorted_airplanes:
    print(i)