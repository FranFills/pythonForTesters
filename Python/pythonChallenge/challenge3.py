"""
Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a Cat and Dog class
that inherits from the Animal class. The Cat and Dog class should override the sound class and print a different sound.
"""


class Animal:

    def get_sound(self, sound):
        self.sound = sound

    sound = 'sssssss'


class Cat(Animal):
    cat_sound = 'meowww'


class Dog(Animal):
    dog_sound = 'Ruff-ruff'


cat = Cat()
print(cat.cat_sound)

dog = Dog
print(dog.dog_sound)
