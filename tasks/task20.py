"""
Create a class called Human
Add an attribute leg_count with the value of 4
Add a method called get_gender() that returns "Unknown" in the Human class
Create another class called Man that extends Human


Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method in each
object instance
"""


class Human:

    leg_count = 4
    get_gender = 'Unknown'

    def print_person_info(self):
        print('\nHuman: ', self.get_gender, self.leg_count)


# child class
class Man(Human):

    def __init__(self, get_gender):
        self.get_gender = get_gender


person1 = Man('Male')
person1.print_person_info()


