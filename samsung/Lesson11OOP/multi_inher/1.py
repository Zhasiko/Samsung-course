from random import randrange


class Engine:
    def __init__(self, volume, cylinderAmount, weight, efficiency, throttleEnergy, breakEnergy):
        self.volume = volume
        self.cylinerAmount = cylinderAmount
        self.weight = weight
        self.efficiency = efficiency
        self.throttleEnergy = throttleEnergy
        self.breakEnergy = breakEnergy

    def getMaxSpeed(self):
        return (self.throttleEnergy - self.breakEnergy) * self.efficiency

class FerrariEngine(Engine):
    def __init__(self, volume, cylinderAmount, weight, efficiency, throttleEnergy, breakEnergy):
        super().__init__(volume, cylinderAmount, weight, efficiency, throttleEnergy, breakEnergy)
        
    def efficiency():
        return 0.25
        
    def throttleEnergy(self):
        return self.volume * self.cylinerAmount * 100
    
    def breakEnergy(self):
        return self.weight * 2
    
    def getMaxSpeed(self):
        return super().getMaxSpeed()
    
    
class RenaultEngine(Engine):
    def __init__(self, volume, cylinderAmount, weight, efficiency, throttleEnergy, breakEnergy, extraTurboEnergy):
        super().__init__(volume, cylinderAmount, weight, efficiency, throttleEnergy, breakEnergy)
        self.extraTurboEnergy = extraTurboEnergy
        
    def efficency():
        return 0.27
    
    def breakEnergy(self):
        return self.weight * 2.1
    
    def getMaxSpeed(self):
        return super().getMaxSpeed()
        
    def throttleEnergy(self):
        return self.volume * self.cylinerAmount * 110 + self.extraTurboEnergy
        
ferrariEng = FerrariEngine(200,1562,3,FerrariEngine.efficiency(),FerrariEngine.throttleEnergy(), FerrariEngine.breakEnergy())
renaultEng = RenaultEngine(555,2325,5, RenaultEngine.efficency(), RenaultEngine.throttleEnergy(), RenaultEngine.breakEnergy(), 5000)

engines = []

engines.append(ferrariEng)
engines.append(renaultEng)

ferrariEng.getMaxSpeed()
# for i in engines:
#     print(i.getMaxEnergy())
        