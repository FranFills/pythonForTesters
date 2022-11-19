"""
Create a class called Utilities
Create a static method called print_name which accepts a parameter, and prints out the parameter.
Invoke the static method print_name()

You can use any of the two methods to create your static methods.
"""


# static methods (methods bound to class rather than class objects)
class Utilities:

    @staticmethod
    def print_name(name):
        return name

    def printname(name):
        return name

Utilities.printname = staticmethod(Utilities.printname)

print('Biller is', Utilities.printname('IBEDC'))
print('Biller is', Utilities.print_name('IKEDC'))

"""
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0 & year % 4 == 0:
      return leap

year = int(input())

def is_leap(year):
    leap = False


# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return leap

# not divided by 100 means not a century year
# year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        return leap

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
    else:
       return not leap

    return leap


year = int(input("Enter a year: "))

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(i,end='')
"""

