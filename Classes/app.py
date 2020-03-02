from collections import namedtuple
from abc import ABC, abstractmethod


class Point:
    # this is an example of a class level attribute
    default_color = "red"

    # self is a reference to the current object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # example of a magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # this is a factory method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Point.default_color = "yellow"
# point = Point(10, 20)
# point = Point.zero()
# print(point.default_color)
# point.draw()


# another = Point(1, 2)
# print(another.default_color)
# another.draw()

# print(point + another)

# print(type(point))
# print(isinstance(point, int))

class TagCloud:
    # double underscores is Python's way of denoting private fields
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getItem__(self, tag):
        return self.__tags.get(tag.lower, 0)

    def __setItem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        # if you don't want to method override, you need to call the super + method that you want
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):

    def swimo(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# This is a bad example of multiple inheritance cause they implement the same methods
class Manager(Employee, Person):
    pass


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


# This is a better example of a multiple inheritance purpose
class FlyingFish(Flyer, Swimmer):
    pass


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

# if you set an abstract method, you must implement that method in all sub classes that borrow from it
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading from a memory stream")


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropDownList(UIControl):
    def draw(self):
        print("Dropdown List")


def draw(controls):
    for control in controls:
        control.draw()


class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


# if a class is just data, you can potentially use the nametuple function
# however this is immutable so you can't change values after they are created
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
