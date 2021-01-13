import math

# Day 2: 30 Days of python programming

# Level 1
"""Exercises: Level 1
	Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
	Write a python comment saying 'Day 2: 30 Days of python programming'
	Declare a first name variable and assign a value to it
	Declare a last name variable and assign a value to it
	Declare a full name variable and assign a value to it
	Declare a country variable and assign a value to it
	Declare a city variable and assign a value to it
	Declare an age variable and assign a value to it
	Declare a year variable and assign a value to it
	Declare a variable is_married and assign a value to it
	Declare a variable is_true and assign a value to it
	Declare a variable is_light_on and assign a value to it
	Declare multiple variable on one line
"""
first_name = str(input('Please Enter your First name: '))
last_name = str(input('Please Enter your Last name: '))
full_name = first_name + ' ' + last_name
country = str(input('Please Enter your country: '))
city = str(input('Please Enter your city: '))
age = str(input('Please Enter your age: '))
is_married = True
is_true = True
is_light_on = True
var_1, var_2, var_3 = 1, 2, 3

# Level 2
"""Check the data type of all your variables using type() built-in function
	Using the len() built-in function find the length of your first name
	Compare the length of your first name and your last name
	Declare 5 as num_one and 4 as num_two
	Add num_one and num_two and assign the value to a variable _total
	Subtract num_two from num_one and assign the value to a variable _diff
	Multiply num_two and num_one and assign the value to a variable _product
	Divide num_one by num_two and assign the value to a variable _division
	Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
	Calculate num_one to the power of num_two and assign the value to a variable _exp
	Find floor division of num_one by num_two and assign the value to a variable _floor_division
"""
print('first_name', type(first_name), first_name)
print('last_name', type(last_name), last_name)
print('full_name', type(full_name), full_name)
print('country', type(country), country)
print('city', type(city), city)
print('age', type(age), age)
print('is_married', type(is_married), is_married)
print('is_true', type(is_true), is_true)
print('is_light_on', type(is_light_on), is_light_on)
print('var_1', type(var_1), var_1)
print('var_2', type(var_2), var_2)
print('var_3', type(var_3), var_3)

print('len first_name', len(first_name), first_name)
print('len first_name > last_name', len(first_name) > len(last_name), first_name, last_name)

num_one = 5
num_two = 4
variable_total = num_one + num_two
variable_diff = num_two - num_one
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainer = num_two % num_one
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two

print('num_one', num_one)
print('num_two', num_two)
print('variable_total', variable_total)
print('variable_diff', variable_diff)
print('variable_product', variable_product)
print('variable_division', variable_division)
print('variable_remainer', variable_remainer)
print('variable_exp', variable_exp)
print('variable_floor_division', variable_floor_division)

# level 3
"""The radius of a circle is 30 meters.
	Calculate the area of a circle and assign the value to a variable area_of_circle
	Calculate the circumference of a circle and assign the value to a variable circum_of_circle
	Take radius as user input and calculate the area.
	Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
"""
radius = float(input('Please Enter the radius of a circle: '))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print('The area of circle = ', area_of_circle)
print('The circumference of circle = ', circum_of_circle)