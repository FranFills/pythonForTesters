
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