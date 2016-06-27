import random
from collections import deque
from Car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

class CarRental(object):

    # Create dictionaries to hold available cars and rented cars. Create tuples of available car makes and colours. Not going to change so don't need lists
    def __init__(self):
        self.available_cars = dict()
        self.rented_cars = dict()
        self._colours = ('Silver', 'Black', 'Blue', 'Grey')
        self._make = ('Toyota', 'BMW', 'Nissan')
        self.type_IDs = ('P', 'D', 'E', 'H')
        
    # Create a deque of cars of type type and of length num, assigning random colour, make and mileage
    # Using deque as it is more efficient to pop from the left of a deque than a list and I want to rotate stock - don't want to rent the same car each time
    def create_cars(self, num, type):
        car_list = deque()
        for i in range(num):
            car = type()
            car.setColour(random.choice(self._colours))
            car.setMake(random.choice(self._make))
            car.setMileage(random.randrange(0, 10000))
            car_list.append(car)
        return car_list
    
    # Create stock by inserting deques of cars into a dictionary where the car types are identified by the keys and the deques of cars are the values. 
    # The keys are P with value PetrolCar deque, D with value DieselCar deque, E with value ElectricCar deque and H with value HybridCar deque    
    def create_stock(self):
        self.available_cars['P'] = self.create_cars(24, PetrolCar)
        self.available_cars['D'] = self.create_cars(8, DieselCar)
        self.available_cars['E'] = self.create_cars(4, ElectricCar)
        self.available_cars['H'] = self.create_cars(4, HybridCar)
    
    # Count the number of cars of type identifier, type_ID, available to rent  
    def count_stock(self, type_ID):
        return len(self.available_cars[type_ID])
    
    # Returns True if num number of cars of type type_ID are available to rent. Returns false if less than this number are available
    def is_in_stock(self, type_ID, num):
        if type_ID in self.type_IDs and isinstance(num, int):
            return num <= self.count_stock(type_ID)
        else:
            raise ValueError
    
    # Removes a car from the left of the deque of available cars of type identified by type_ID 
    def get_car(self, type_ID):
        if type_ID in self.type_IDs:
            return self.available_cars[type_ID].popleft()
        else:
            raise ValueError    
        
    # Check if car is Petrol, Diesel, Electric or Hybrid and return identifier
    def check_car_type(self, car):
        if isinstance(car, PetrolCar):
            return 'P'
        elif isinstance(car, DieselCar):
            return 'D'
        elif isinstance(car, ElectricCar):
            return 'E'
        elif isinstance(car, HybridCar):        
            return 'H'
        else:
            raise ValueError
    
    # Remove num_cars number of cars of type type_ID from available cars, add to list booking_list and return. Raise ValueError if arguments not as expected
    def get_booking_list(self, num_cars, type_ID):
        if  isinstance(num_cars, int) and type_ID in self.type_IDs:
            booking_list = list()
            for i in range(num_cars):
                rented_car = self.get_car(type_ID) 
                booking_list.append(rented_car)
            return booking_list
        else:
            raise ValueError
    
    # Take number and typeID of cars required, create booking reference and booking_list. 
    # Add the booking reference to dictionary rented_cars as a key where another dictionary of list of cars (booking_list) and customer name is the value
    def process_rental(self, num_cars, type_ID, cust_name):        
        booking_ref = random.randrange(1000, 2000)
        booking_list = self.get_booking_list(num_cars, type_ID)
        self.rented_cars[booking_ref] = {'car': booking_list, 'customer name': cust_name } 
        return booking_ref 

    # Take booking reference, pop the booking associated with it from rented_cars. For the list of cars in the booking, check the type of car and append 
    # each back on to the correct deque in available_cars. 
    def process_return(self, ref):
        booking = self.rented_cars.pop(ref)
        for car in booking['car']:
            type_ID = self.check_car_type(car)
            self.available_cars[type_ID].append(car) 


   