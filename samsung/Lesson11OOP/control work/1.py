class Store:
    def __init__(self, name, city, tovary,numofTovar):
        self.name = name
        self.city = city
        self.tovary = tovary
        self.numofTovar = numofTovar
        
    def checkTovars(self):
        for i in self.tovary:
            print(i,end = " ")
        print()
        
class Tovar:
    def __init__(self,id,name,type,cost):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost
        
    def __str__(self):
        return self.name
    
                
        
class Admin():
    def __init__(self, name):

        self.name = name
        
    def add(self,store,tovar):
        store.tovary.append(tovar)
        
    def remove(self,store,tovar):
        store.tovary.remove(tovar)
        
class Salesman():
    def __init__(self, name,  store):
        self.name = name
        self.store = store
        
    def add(self,tovar):
        self.store.tovary.append(tovar)
        
    def remove(self,tovar):
        self.store.tovary.remove(tovar)
        
    def checkBucket(self,Bucket):
        for i in Bucket.bucket:
            print(i,end = " ")
        print(str(Bucket.amount))

class Customer():
    def __init__(self, name, store, money):
        self.name = name
        self.store = store
        self.money = money
        
    def getMoney(self,summa):
        self.money += summa
    
    def addTovartoBucket(self,tovar,Bucket):
        Bucket.bucket.append(tovar)
        Bucket.amount += tovar.cost
    
    def removeTovarfromBucket(self,tovar,Bucket):
        Bucket.remove(tovar)
        Bucket.amount -= tovar.cost
    
    def buy(self,Bucket):
        self.money = self.money - Bucket.amount
        for i in Bucket.bucket:
            self.store.tovary.remove(i)
        Bucket.bucket.clear()
        Bucket.amount = 0
        
        
class Bucket:
    def __init__(self,bucket,amount):
        self.bucket = bucket
        self.amount = amount
        
    
tovar1 = Tovar(45,'snickers','chocolate',200)
tovar2 = Tovar(88,"soap",'soap',150)
tovar3 = Tovar(54,'cola','drink',300)
    
tovaryAlma = [tovar1,tovar2,tovar1,tovar2, tovar3]
    
storeAlma = Store("Alma","Alamty",tovaryAlma,len(tovaryAlma))

adminAlma = Admin('Tray')

salesmanAlma = Salesman('Zhazira',storeAlma)

customerFromAlmaty = Customer('Katya',storeAlma,1500)

bucketAlma = Bucket([],0)

# adminAlma.add(storeAlma,tovar3)
# storeAlma.checkTovars()
# print()
# adminAlma.remove(storeAlma,tovar2)
# storeAlma.checkTovars()
# print()

# salesmanAlma.add(tovar1)
# storeAlma.checkTovars()
# salesmanAlma.remove(tovar1)
# print()
# storeAlma.checkTovars()

# customerFromAlmaty.getMoney(1000)
# print(customerFromAlmaty.money)

# customerFromAlmaty.addTovartoBucket(tovar1,bucketAlma)
# customerFromAlmaty.addTovartoBucket(tovar2,bucketAlma)
# salesmanAlma.checkBucket(bucketAlma)

# customerFromAlmaty.buy(bucketAlma)
# print(customerFromAlmaty.money)
# salesmanAlma.checkBucket(bucketAlma)
# storeAlma.checkTovars()