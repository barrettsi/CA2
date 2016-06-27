from car_Rental import CarRental

# Print instruction (string) for user and get input. Check the input is one of the accepted inputs (accepted_values) and change it to type type or str if no input
def get_accepted_input(string, accepted_values, type = str):
    while True:
        option = type(raw_input(string).upper())
        if option in accepted_values:
            break
        else:
            print 'That is not a valid option'
    return option

# Print instruction (string) for user and get input of type integer - no accepted values   
def get_num_input(string):
    while True:
        s_inp = raw_input(string)
        try:
            num = int(s_inp)
            break
        except:
            print 'That is not a valid input.'        
    return num  

# Print the details of the booking linked to the booking reference    
def print_booking_details(booking_ref):
    print ('Your booking details are as follows:\n'
        'Booking reference: {}. You will need this to return your car(s).\n'
        'Customer name: {}'.format(booking_ref, rental.rented_cars[booking_ref]['customer name']) 
        )
    for i, car in enumerate(rental.rented_cars[booking_ref]['car']):
        print ('Car no: {}\n'
                'Car make: {}\n'
                'Car colour: {}\n'.format(i + 1, car.getMake(), car.getColour() )
                )
                
# Instantiate CarRental and initialise stock   
rental = CarRental()
rental.create_stock()
proceed = 'Y'

# User interface
print 'Welcome to DBS Car Rental.' 
while proceed == 'Y':
    choice = get_accepted_input('Please choose from the following options: \n - Type RENT to rent a car \n - Type RETURN to return a car\n', ('RENT', 'RETURN')) 
    if choice == 'RENT':
        type_ID = get_accepted_input('What type of car would you like to rent? \n Type P for petrol \n Type D for diesel \n Type E for electric \n Type H for hybrid \n', rental.type_IDs)
        num_cars = get_num_input('Please enter number of cars you wish to rent: ')
        if rental.is_in_stock(type_ID, num_cars):
            cust_name = raw_input('Please enter your name: ')
            booking_ref = rental.process_rental(num_cars, type_ID, cust_name)  
            print_booking_details(booking_ref)
        else:
            print 'Unfortunately we do not have {} cars of type {} in stock. We currently have {}.'.format(num_cars, type_ID, rental.count_stock(type_ID))
    else:
        if len(rental.rented_cars) == 0:
            print 'You have not yet rented any cars. Please first choose to rent.'
            continue
        ref = get_accepted_input('To return your rented car(s) please enter your booking reference: ', rental.rented_cars.keys(), int)
        print_booking_details(ref)
        rental.process_return(ref)
        print 'Your rental(s) have been returned.'
    proceed = get_accepted_input('Would you like to carry out another transaction?\n Type Y for Yes or N for No \n', ('Y', 'N'))
print 'Thank you for using DBS Car Rental.'
