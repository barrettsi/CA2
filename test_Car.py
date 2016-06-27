import unittest
from collections import deque
from car_Rental import CarRental
from Car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

#Test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
     
    # Testing getMileage and setMileage methods  
    # Tests mileage is initially 0
    # Tests mileage = 15,000 after using set method to set it to 15,000 
    # Tests setMileage will give an error if given input of type string 
    # Tests setMileage will give an error if called with too many arguments
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.setMileage(15000)
        self.assertEqual(15000, self.car.getMileage())
        self.assertRaises(ValueError, self.car.setMileage, '2')
        self.assertRaises(TypeError, self.car.setMileage, 10000, 1500)
    
    # Tests the setMake and getMake methods
    # Use getMake to tests make is initially set to default value ''
    # Use setMake to change make to Ferrari and then use getMake to check the value is now Ferrari
    # Test getMake raises typeError when called with an argument
    # Test setMake raises typeError when called with too many arguments
    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
        self.assertRaises(TypeError, self.car.getMake, 'Ferrari')
        self.assertRaises(TypeError, self.car.getMake, 'Ferrari', 'Enzo')
    
    # Tests the getColour and setColour methods
    # Tests getColour returns default value of colour ''
    # Tests colour is 'Silver' after using setColour to set to 'Silver' and getColour to return the value of colour 
    # Tests getColour raises TypeError when called with an argument
    # Tests setColour raises TypeError when called with too many arguments
    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.setColour('Silver')
        self.assertEqual('Silver', self.car.getColour())
        self.assertRaises(TypeError, self.car.getColour, 'blue')
        self.assertRaises(TypeError, self.car.setColour, 'blue', 'green')
        
#Test the ElectricCar functionality
class TestElectricCar(unittest.TestCase):

    def setUp(self):
        self.electric_car = ElectricCar()	
    
    # Test the getNumberFuelCells and setNumberFuelCells methods
    # Test getNumberFuelCells returns the default number of fuel cells, 1
    # Use setNumberFuelCells to change the value to 8 and test the value has now changed using getNumberFuelCells
    # Test setNumberFuelCells raises valueError when given an argument of the wrong type - string instead of int or float
    # Test setNumberFuelCells raises typeError when called with too many arguments
    def test_electric_car_fuel_cells(self):
        self.assertEqual(1, self.electric_car.getNumberFuelCells())
        self.electric_car.setNumberFuelCells(8)
        self.assertEqual(8, self.electric_car.getNumberFuelCells())
        self.assertRaises(ValueError, self.electric_car.setNumberFuelCells, '6')
        self.assertRaises(TypeError, self.electric_car.setNumberFuelCells, 2, 4)
    
    # Test the getMileage and setMileage methods inherited from superclass Car work in the subclass  
    # Test getMileage returns default value of 0
    # Use setMileage to change mileage to 460000 and then use getMileage to test that the value has changed
    # Test setMileage raises a ValueError when called with string argument
    def test_electric_car_mileage(self):
        self.assertEqual(0, self.electric_car.getMileage())
        self.electric_car.setMileage(460000)
        self.assertEqual(460000, self.electric_car.getMileage())
        self.assertRaises(ValueError, self.electric_car.setMileage, '60000')

#Test the PetrolCar        
class TestPetrolCar(unittest.TestCase):
            
    def setUp(self):
        self.petrol_car = PetrolCar()

    # Test the getNumberCylinders and setNumberCylinders methods
    # Use getNumberCylinders to test it returns the correct default value ''
    # Use setNumberCylinders to change value to 16 and then use getNumberCylinders to test it returns the new value
    # Test a ValueError is returned if setNumberCylinders is called with the wrong type of argument
    # Test a TypeError is returned if setNumberCylinders is called with the wrong number of arguments
    def test_petrol_car_cylinders(self):
        self.assertEqual(8, self.petrol_car.getNumberCylinders())
        self.petrol_car.setNumberCylinders(16)
        self.assertEqual(16, self.petrol_car.getNumberCylinders())
        self.assertRaises(ValueError, self.petrol_car.setNumberCylinders, '12')
        self.assertRaises(TypeError, self.petrol_car.setNumberCylinders, 12, 6)
    
    # Test the getMake and setMake methods inherited from superclass Car work in the subclass PetrolCar
    # Test the getMake method returns the default value of make ''
    # Use setMake to change make to Ford and then use getMake to check the value is now Ford
    def test_petrol_car_make(self):
        self.assertEqual('', self.petrol_car.getMake())
        self.petrol_car.setMake('Ford')
        self.assertEqual('Ford', self.petrol_car.getMake())

#Test DieselCar functionality        
class TestDieselCar(unittest.TestCase):  
    
    def setUp(self):
        self.diesel_car = DieselCar()
    
    # Test of the getNumberGlowPlugs and setNumberGlowPlugs methods
    # Use getNumberGlowPlugs to check it is correctly set to default number 1
    # Use setNumberGlowPlugs to change the value and then use getNumberGlowPlugs to check the value has changed correctly
    # Tests a valueError is raised if setNumberGlowPlugs is called with input that isn't int or float
    # Tests TypeError is raised if setNumberGlowPlugs is called with too many inputs
    def test_diesel_car_glow_plugs(self):
        self.assertEqual(1, self.diesel_car.getNumberGlowPlugs())
        self.diesel_car.setNumberGlowPlugs(6)
        self.assertEqual(6, self.diesel_car.getNumberGlowPlugs())
        self.assertRaises(ValueError, self.diesel_car.setNumberGlowPlugs, 'six')
        self.assertRaises(TypeError, self.diesel_car.setNumberGlowPlugs, 'six', 2)

#Test HybridCar        
class TestHybridCar(unittest.TestCase):
    
    # SetUp to create an instance of HybridCar    
    def setUp(self):
        self.hybrid_car = HybridCar()
    
    # Test of the getTypeHybridBattery and setTypeHybridBattery methods
    # Use the getTypeHybridBattery method to check that the default value is set to 'Lithium-Ion'
    # Set the value to 'Nickel-Metal Hydride' using setTypeHybridBattery and then use getTypeHybridBattery to check that the value has changed as expected  
    # A TypeError is raised if getTypeHybridBattery or setTypeHybridBattery are called with too many arguments
    def test_hybrid_car_hybrid_battery(self):
        self.assertEqual('Lithium-Ion', self.hybrid_car.getTypeHybridBattery())
        self.hybrid_car.setTypeHybridBattery('Nickel-Metal Hydride')
        self.assertEqual('Nickel-Metal Hydride', self.hybrid_car.getTypeHybridBattery())
        self.assertRaises(TypeError, self.hybrid_car.getTypeHybridBattery, 1)
        self.assertRaises(TypeError, self.hybrid_car.setTypeHybridBattery, 'battery', 'another type')

#Test functions in CarRental        
class TestCarRental(unittest.TestCase):

    # SetUp to create an instance of CarRental
    # Use create_stock to initialise available_cars
    # Call process_rental with sample input (3 cars, type Petrol, Customer name Tom Murphy) and assign returned booking reference to test_ref. 
    # Need to have rented cars in order to test return process  
    def setUp(self):
        self.rental = CarRental()
        self.rental.create_stock()
        self.rental.test_ref = self.rental.process_rental(3, 'P', 'Tom Murphy')
    
    # Test that create_cars creates a deque of cars of the right type and length
    # The length of the deque should be the same as the number of cars specified
    # Tests all elements of the deque are of the type specified e.g. all of type PetrolCar
    # Tests all elements of the deque have been assigned a make i.e. none have the default make value ''
    # A TypeError is raised if the function is called with more than 2 arguments
    # A TypeError is raised if the function is called with the wrong type of arguments
    def test_create_cars(self):
        car_deque = self.rental.create_cars(20, PetrolCar)
        self.assertEqual(20, len(car_deque))
        self.assertTrue(all(isinstance(car, PetrolCar) for car in car_deque))
        self.assertTrue(all(car.getMake != '' for car in car_deque))
        self.assertRaises(TypeError, self.rental.create_cars, 20, PetrolCar, 2)
        self.assertRaises(TypeError, self.rental.create_cars, 20, 2)
    
    # Test create_stock creates a dictionary where the keys are P, D, E, H and the values are deques of cars
    # Test that create_stock makes a dictionary of length 4
    # Tests that each value in the key-value pairs in the dictionary is of type deque
    # Test each of the key value pairs in the dictionary are as expected - 
    # for key P, value is deque of length 21 (not 24 due to process_rental method called in setUp)
    # for key D, value is deque of length 8
    # for key E, value is deque of length 4
    # for key H, value is deque of length 4
    def test_create_stock(self):
        self.assertEqual(4, len(self.rental.available_cars))
        self.assertTrue(all(isinstance(value, deque) for value in self.rental.available_cars.values()))
        self.assertEqual(21, len(self.rental.available_cars['P']))
        self.assertEqual(8, len(self.rental.available_cars['D']))
        self.assertEqual(4, len(self.rental.available_cars['E']))
        self.assertEqual(4, len(self.rental.available_cars['H']))

    # Test count_stock method - takes a car type identifier as an argument and returns the number of cars of that type in stock
    # Test the method returns the correct value, 4,  for H, Hybrid cars
    # Test the method returns the correct value, 8,  for D, Diesel cars
    # Test the method returns the correct value, 4,  for E, Electric cars
    # Test the method returns the correct value, 21,  for P, Petrol cars
    def test_count_stock(self):
        self.assertEqual(4, self.rental.count_stock('H'))
        self.assertEqual(8, self.rental.count_stock('D'))
        self.assertEqual(4, self.rental.count_stock('E'))
        self.assertEqual(21, self.rental.count_stock('P'))

    # Test the is_in_stock method - takes a car type identifier and number as arguments and returns true if that number of cars of that type are in stock
    # Returns True when asked to check if 5 petrol cars are in stock
    # Returns True when asked to check if 8 diesel cars are in stock
    # Returns False when asked to check if 10 hybrid cars are in stock (total Hybrids = 4)
    # Raises ValueError when given invalid type identifier
    def test_is_in_stock(self): 
        self.assertTrue(self.rental.is_in_stock('P', 5))
        self.assertTrue(self.rental.is_in_stock('D', 8))
        self.assertFalse(self.rental.is_in_stock('H', 10))
        self.assertRaises(ValueError, self.rental.is_in_stock, HybridCar, 10)
        
    # Test the get_car method - takes car type identifier as an argument and removes and returns a car of that type from the available stock
    # Test that the method returns a car of type PetrolCar when called with the type identifier for PetrolCar
    # Test that the method does not return a car of type PetrolCar when called with the type identifier for HybridCar
    # Test that method returns a ValueError when called with an argument which is not one of the type identifiers
    def test_get_car(self): 
        self.assertEqual(PetrolCar, type(self.rental.get_car('P')))
        self.assertNotEqual(PetrolCar, type(self.rental.get_car('H')))
        self.assertRaises(ValueError, self.rental.get_car, 'Hybrid')
        
    # Test the check_car_type method - takes car as argument and returns type identifier
    # Test the method returns correct type identifier 'E' when called with an instance of ElectricCar
    # Test the method returns a ValueError when given input which is not a car type identifier
    def test_check_car_type(self): 
       self.assertEqual('E', self.rental.check_car_type(ElectricCar()))
       self.assertRaises(ValueError, self.rental.check_car_type, 'Electric')

    # Test the get_booking_list method - takes number of cars and type_ID as arguments and returns a list of cars of that type of num_cars length
    # Create a booking_list to test
    # Test the method returns a list of the correct length
    # Tests the method returns list of the correct type
    # Test the method returns a ValueError if called with invalid arguments - string '5' instead of number
    def get_booking_list(self): 
        test_list = self.rental.get_booking_list(5, 'D')
        self.assertEqual(5, len(test_list))
        self.assertTrue(all(isinstance(car, DieselCar) for car in test_list))
        self.assertRaises(ValueError, self.rental.get_booking_list('5', 'D'))
        
    # Test the process_rental method - takes a number of cars, a car type identifier and a customer name as arguments, creates a random number booking ref
    # and uses this as the key for the dictionary where the booking details (list of cars rented and customer name) are stored.
    # Called in setUp as self.rental.test_ref = self.rental.process_rental(3, 'P', 'Tom Murphy'). Arguments are 3 cars, type Petrol, Customer name Tom Murphy
    # Test that the returned ref, test_ref, is an int
    # Test that the length of the list of rented cars held in the dictionary corresponding to test_ref is equal to the specified number of cars, 3
    # Test that each of the cars in the list is of the correct type 'P'
    # Test that customer name 'Tom Murphy' has been correctly assigned in the dictionary corresponding to test_ref
    # Tests that this method has reduced the number of petrol cars in available_cars to 21
    # Test that the method raises a TypeError if given the incorrect number of arguments
    def test_process_rental(self):   
        self.assertIsInstance(self.rental.test_ref, int)
        self.assertEqual(3, len(self.rental.rented_cars[self.rental.test_ref]['car']))
        self.assertTrue(all(isinstance(car, PetrolCar) for car in self.rental.rented_cars[self.rental.test_ref]['car']))
        self.assertEqual('Tom Murphy', self.rental.rented_cars[self.rental.test_ref]['customer name'])
        self.assertEqual(21, len(self.rental.available_cars['P']))
        self.assertRaises(TypeError, self.rental.process_rental, 4, 'H')
    
    # Test the process_return method - takes a booking reference as an argument
    # Call process_return with test_ref (defined in setUp) as argument. This is a reference to a booking for 3 petrol cars
    # Tests the length of rented_cars is 0 after the cars have been returned 
    # Tests the available_cars number of petrol cars has increased to 24 after the cars have been returned - i.e. correct number of cars added to correct deque
    def test_process_return(self): #, ref):
        self.rental.process_return(self.rental.test_ref)
        self.assertEquals(0, len(self.rental.rented_cars))
        self.assertEquals(24, len(self.rental.available_cars['P']))

if __name__ == '__main__':
    unittest.main()