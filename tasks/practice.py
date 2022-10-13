
fruits = ['Apple', 'Banana', 'Cucumber']
for fruit in fruits:
    print('Fruit: ' + fruit)

name = 'Stadium'
for c in name:
    print('Character: ' + c)

number = 13
while 0 < number: #< 12:
    print('number: ', number)
    number -= 1

def greet():
    print('Hello World from python')

greet()

def accept(cd):
    cd('Hello Dear')

hello = lambda : print('Hello World Anonymous')
hello()

accept(lambda c: print(c))

def num (num1, num2=4):
    print(num1 + num2)

num(3, 9)

# required parameter
def greet (name):
    print('Hello', name)

greet('Fisayo')

# default parameter
def sumOfNumbers(firstNum =21, secondNum =12):
    addResult = firstNum+secondNum
    print('Result', addResult)

sumOfNumbers()

# keyword parameter
def sumNumbers(firstNum, secondNum):
    addResult = firstNum-secondNum
    print('Result', addResult)

sumNumbers(secondNum = 16, firstNum=11 )


# arbitrary parameter
def sNumbers(*args):
    print('Args', args)

sNumbers()
sNumbers(0, 87, 32)
sNumbers(7, 21, 65)
sNumbers(2, 5, 7, 9, 'Hello')

# Global variable
name = 'Testify'

def language():
    curr_lang = 'Python' # Local variable
    print('Name', name, 'Language', curr_lang)

def framework():
    curr_framework = 'Selenium' # Local variable
    print('Name', name, 'Framework', curr_framework)

language()
framework()

def reduce_number_loop(num):
    while num>=0:
        print(num)
        num -=1

def reduce_number_recursion(num):
    print(num)
    #num -=1
    if num == 0:
        return
    reduce_number_recursion(num-1)

reduce_number_loop(6)
print()
reduce_number_recursion(7)

name = '  testify operations: switch to software testing  '

# length: print the length of a string
print(len(name))

# upper: convert a string to uppercase
print(name.upper())

# lower: convert a string to lowercase
print(name.lower())

# capitalize: convert first char to uppercase
print(name.capitalize())

#count: count the occurence of a value in a string
print(name.count(' '))

# find: index of position of a value, if value is not in the string, it returns -1
print(name.find('for'))

# index: index of position of a value, if value is not in the string, it throws an exception
print(name.index('to'))

# strip: remove excess whitespace at the beginning and end of a string
print(name)
print(name.strip())

# rstrip: remove excess whitespace at the end of a string
print(name)
print(name.rstrip())

# lstrip: remove excess whitespace at the beginning of a string
print(name)
print(name.lstrip())

# split: split a string to an array using the specified value
print(name.split(' '))

# format: format the specified value of a string
# named format
unformatted = 'My name is {name}, I am a {occupation}'
formatted = unformatted.format(name='Fisayo', occupation='Tester')
print(formatted)

# indexed format
unformatted = 'My name is {0}, I am a {1}'
formatted1 = unformatted.format('Fisayo', 'Automation Engineer')
print(formatted1)

# unindexed format
unformatted = 'My name is {}, I am a {}'
formatted2 = unformatted.format('Fisayo', 'Engineer')
print(formatted2)

languages = ['C', 'python', 'java', 'C#', 'C++']
print(languages)

# append: add new item to the list
languages.append('Javascript')
print(languages)

# insert: add new item to specified position
languages.insert(0, 'C')
languages.insert(2, 'PHP')
print(languages)

# pop: remove item to specified position(if position is noty specified, last item in the list is removed)
languages.pop(0)
languages.pop()
print(languages)

# remove: remove item by value
languages.remove('PHP')
#languages.insert(2, 'PHP')
print(languages)

# count: return the number of occurrence of an item in a list
languages.count('C')
#languages.insert(2, 'PHP')
print(languages.count('C++'))

# len: count the number of items in a list
length = len(languages)
print(length)

# clear: delete all items in a list
clear = languages.clear()
length = len(languages)
print(languages, length)

# copy: return a copy of the list
languages = ['C', 'python', 'java', 'C#', 'ruby', 'javascript']
print(languages)
print(languages.copy())

# reverse: return a copy of the list in reverse order
print(languages)
languages.reverse()
print(languages)

# sort: sort the items in a list by ascending or descending order
# sort ascending
languages.sort()
print(languages)

# sort descending
languages.sort(reverse=True)
print(languages)

# extend: add contents of a specified list to current list
languages.extend([12, 'football', 'sql', 'typescript'])
print(languages)
biodata = {
    'name': 'Fisayo',
    'age': 21,
    'marital_status': 'single',
    'occupation': 'Test Automation Engineer'
}

print(biodata)


# get: fetch a value using specified key
print(biodata.get('name'))

# items: return list of key value pairs as a tuple
print(biodata.items())

# keys: return keys as a list
print(biodata.keys())

# value: return vlaues as a list
print(biodata.values())

# pop: remove key:value pair from the dictionary
popDict = biodata.pop('name')
print(biodata)

# update: add more key:value pair to the dictionary
updateDict = biodata.update({'complexion': 'Dark', 'Bestie': 'Diane'})
print(biodata)

# popItem: remove the last key:value pair from the dictionary
popItemDict = biodata.popitem()
print(biodata)

# copy: returns a copy of the dictionary
biodata_copy = biodata.copy()
print(biodata_copy)

# clear: removes all the elements of a dictionary
biodata.clear()
print(biodata)
print(biodata_copy)

# class
class Human:

    name = 'homo sapiens'
    group = 'Mammal'
    blood = 'warm blooded'

    def get_name(self):
        return self.name + ':' + self.group + ':' + self.blood

# objects
Lanre = Human()

print(Lanre.name, Lanre.group, Lanre.get_name())

class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name

fisayo = Human('Fisayo')
print(fisayo.can_walk)
print(fisayo.leg_count)
print(fisayo.name)

class Animal:

    leg_count = 4
    group = 'Mammal'

# default constructor
    def __init__(self):
        self.name = 'Unknown'


class Vehicle:

    can_fly = False
    tire_count = 4

# parameterized constructor
    def __init__(self, make):
        self.make = make

    def set_tire_count(self, count):
        self.tire_count = count

    def set_flyable(self, cfly):
        self.can_fly = cfly

    def get_make_tire_count(self):
        return self.make + ':' + str(self.tire_count)

    def check_type(self):
        if self.make == 'Aeroplane':
            print('This is a plane')
        else:
            print('This is probably a car')

toyota = Vehicle('Toyota')
print('\nVehicle:', toyota.make, toyota.can_fly)
toyota.check_type()

lexus = Vehicle('Lexus')
print('\nVehicle:', lexus.make, lexus.can_fly)


plane = Vehicle('Aeroplane')
plane.set_tire_count(7)
plane.set_flyable(True)
print('\nVehicle:', plane.make, plane.tire_count, plane.can_fly)
print(plane.get_make_tire_count())

plane.check_type()

# Inheritance
class Vehicle:

    model = 'Unknown'
    make = 'Unknown'
    production_year = '1990'

    def print_vehicle_info(self):
        print('\nVehicle: ', self.make, self.model, self.production_year)


# child class
class Car(Vehicle):

    wheel_count = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

# Polymorphism
class Plane(Vehicle):

    model = 'Aeroplane'
    make = 'Boeing'

vehicle = Vehicle()
vehicle.print_vehicle_info()

car1 = Car('Toyota', 'Camry')
car1.print_vehicle_info()

plane1 = Plane()
plane1.print_vehicle_info()

animal = Animal()
print('\nAnimal:', animal.name, animal.group)


class Vehicle():

    def drive_direction(self):
        print('\nVehicle: ', 'Move forward')


class Plane(Vehicle):

    def drive_direction(self):
        print('\nPlane: ', 'Move upward')


class Submarine(Vehicle):

    def drive_direction(self):
        print('\nSubmarine: ', 'Move downward')

vehicle = Vehicle()
vehicle.drive_direction()

plane1 = Plane()
plane1.drive_direction()

sub_marine = Submarine()
sub_marine.drive_direction()

#data encapsulation
class User:

    __first_name = 'Testify'
    __last_name = 'QA'
    __attendance = 2

    def get_name(self):
        return 'User: ' + self.__first_name

    def get_attendance(self):
        value = self.__attendance * 12
        return 'Attendance: ' + str(value)

user = User()
print(user.get_name())

print(user.get_attendance())

# Data Abstraction
class LoginSession:

    __email = 'user@test.com'
    __password = 'password'

    def get_email(self):
        return self.__email

    def get_password(self):
        return '*********'

session = LoginSession()
print(session.get_email())
print(session.get_password())