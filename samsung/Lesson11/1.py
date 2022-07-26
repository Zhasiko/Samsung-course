def __repr__(self):
    return f"Name: {self.name}"

class CPU:
    def __init__(self,cashMemory,price, weight):
        self.cashMemory = cashMemory
        self.price = price
        self.weight = weight

class HDD:
    def __init__(self,memory,price,weight):
        self.memory = memory
        self.price = price
        self.weight = weight
        
class Laptop:
    def __init__(self, name, price, weight,hardDiskDrive,cpuMemory):
        self.name = name
        self.price = price
        self.weight = weight
        self.hardDiskDrive = hardDiskDrive
        self.cpuMemory = cpuMemory
        
    def getTotalPrice(self):
        return self.price + self.cpuMemory.price + self.hardDiskDrive.price
    
    def getTotalCPUMemory(self):
        return sum(self.cpuMemory)
    
    def getTotalWeight(self):
        return self.weight + self.hardDiskDrive.weight + self.cpuMemory.weight
    
cpu1 = CPU(100,500,200)
cpu2 = CPU(120,400,250)
hdd1 = HDD()
        
        