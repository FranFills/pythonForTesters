
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
