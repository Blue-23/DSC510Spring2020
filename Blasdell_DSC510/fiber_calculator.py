# course: DSC510
# assignment: 2.1
# date: 3/17/20
# name: Blaine Blasdell
# description: Customer Fiber Optic cable calculator

# welcome message
print('Welcome to Blasdell\'s IT Services')
print('\r')
print('Fiber Optic Cable Cost Calculator')
print('\r')

# input customer's company name
company_name = input('Please enter your company name: ')
print('\r')

# input customer's cable need
cable_feet = float(input('Please enter the amount of fiber you need (in feet): '))
print('\r')

# set default cable price
default_price = 0.87
cable_price = default_price

# calculate customer price feet * default price
installation_cost = cable_feet * cable_price


