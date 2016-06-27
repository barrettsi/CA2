#Define car class
class Car(object):
#Implement the car object    

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = '' 
    
    # Returns the colour of the car object
    def getColour(self):
        return self.__colour
    
    # Returns the mileage of the car object
    def getMileage(self):
        return self.__mileage
    
    # Returns the make of the car object
    def getMake(self):
        return self.__make
    
    # Used to set a car's colour
    def setColour(self, colour):
        self.__colour = colour

    # Used to set a car's mileage        
    def setMileage(self, mileage):
        if isinstance(mileage, (int, float)):
            self.__mileage = mileage
        else:
            raise ValueError
            
    # Used to set a car's make        
    def setMake(self, make):
        self.__make = make

#Define electric car class
class ElectricCar(Car):
#Implement the electric car object    

    def __init__(self):	
        Car.__init__(self)
        self.__numberFuelCells = 1
    
    # Used to get an ElectricCar's NumberFuelCells
    def getNumberFuelCells(self):
        return self.__numberFuelCells 
    
    # Used to set an ElectricCar's NumberFuelCells		
    def setNumberFuelCells(self, value):
        if isinstance(value, (int, float)):
            self.__numberFuelCells = value
        else:
            raise ValueError

#Define petrol car class
class PetrolCar(Car):
#Implement the petrol car object    

    def __init__(self):	
        Car.__init__(self)
        self.__numberCylinders = 8
    
    # Used to get a PetrolCar's numberCylinders
    def getNumberCylinders(self):
        return self.__numberCylinders
    
    # Used to set a PetrolCar's numberCylinders    
    def setNumberCylinders(self, value):
        if isinstance(value, (int, float)):
            self.__numberCylinders = value
        else:
            raise ValueError

class DieselCar(Car):
#Implement the diesel car object

    def __init__(self):
        Car.__init__(self)
        self.__numberGlowPlugs = 1
     
    # Used to get a DieselCar's numberGlowPlugs
    def getNumberGlowPlugs(self):
        return self.__numberGlowPlugs

    # Used to set a DieselCar's numberGlowPlugs        
    def setNumberGlowPlugs(self, value):
        if isinstance(value, (int, float)):
            self.__numberGlowPlugs = value
        else:
            raise ValueError
        
        
class HybridCar(Car):
#Implement the hybrid car object

    def __init__(self):
        Car.__init__(self)
        self.__typeHybridBattery = 'Lithium-Ion'
    
    # Used to get a HybridCar's typeHybridBattery
    def getTypeHybridBattery(self):
        return self.__typeHybridBattery
        
    # Used to set a HybridCar's typeHybridBattery        
    def setTypeHybridBattery(self, value): 
        self.__typeHybridBattery = value
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        