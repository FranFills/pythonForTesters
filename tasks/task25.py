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
