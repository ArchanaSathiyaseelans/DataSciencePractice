#classes and objects

from car import Car

car_1 = Car("chevy", "Corvette", "2021", "blue")
car_2 = Car("Ford", "Mustang", "2022", "red")

print(car_1.model)
print(car_1.make)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

Car.wheels = 2

print(car_1.wheels)




#Inheritance

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swin(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.run())
print(rabbit.alive)
print(hawk.fly())
print(fish.swin())

# multi-level inheritance - when a derived class inherits another (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)   # inherited from the Organism class
dog.eat()          # inherited from the Animal class
dog.bark()         # defined in Dog class


#multiple inheritance = when a class is derived from more than one parent class
class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

#method overrifing - overwrites the method of child class that is inhwerited from the parent class

class  Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()


# method chaining - calling multiple methods sequentially each performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return  self

    def drive(self):
        print("You drive tha car")
        return self

    def brake(self):
        print("You stop on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return  self

car = Car()

car.turn_on().drive()
car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()


# super() function - function used to give access to the methods of a parent class
#                     Returns a temporary object of a parent class when used


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, legth, width):
        super().__init__(legth, width)

    def area(self):
        return  self.length*self.width


class Cube(Rectangle):

    def __init__(self, legth, width, height):
        super().__init__(legth, width)
        self.height = height

    def volume(self):
        return self.length * self.width*self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

# Prevents a user from creating an object of that class
# + comples a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vechicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vechicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vechicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()



#Object as arguments
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(bike_1.color)

# Duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like aduck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("this duck is qwacking")


class Chicken:

    def walk(self):
        print("This Chicken is walking")

    def talk(self):
        print("this Chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("Yes caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)


# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assign values to variables as part of a larger expression

happy = True
print(happy)

print(happy:=False) # used := walrus operator

foods = list()
while True:
    food = input("What food do yoy like?: ")
    if food == "quit":
        break
    foods.append(food)


# using walrus method

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)


# functions to variables

def hello():
    print("Hello")

hi = hello
hello()
hi()

say = print
say("Whao! I can't belive this works: 0")

# Higher Order function = a function that either:
#                          1. accepts a function as an argument
#                            or
#                          2. returns a function
#                           (In python , function are also trated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello everyone")
    print(text)

hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(7))


#lamda function = function written in 1 line using lambda keyword
#                 accepts any number of arguments, but only has one expression,
#                 (thinks of its as a shortcut)
#                 (useful if needed for a short period of time, throe-away)
# lambda parameters:expression

double = lambda x:x * 2
multiply = lambda x, y: x + y
add = lambda x, y, z: x + y + z
full_name = lambda firstname, lastname: firstname+ " " +lastname
age_check = lambda age:True if age >= 18 else False

print(age_check(18))


# sort() Method = used with lists
# sort() function = used with iterables

students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
#students.sort(reverse = True)

sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)


students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda ages:ages[2]
#students.sort(key=age, reverse=True)
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)

# map() = applies a function to each item in an iterable(list, tuple, etc.)

#map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)

# filter() = creates a collection of elements from an iterable for which a function returns true

# filter(function, iterable)

friends = [("Rachel", 10),
           ("Monica", 19),
           ("Phoeba", 17),
           ("Joey", 18),
           ("Chandler", 21),
           ("Ross", 20)
           ]

age = lambda data:data[1] >= 18

driking_buddies = list(filter(age, friends))

for i in driking_buddies:
    print(i)

#reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#           performs function on first the elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y,:x + y, letters)
print(word)

factorial = [5, 6, 7, 8, 9]
result = functools.reduce(lambda x, y, : x * y, factorial)
print(result)

# list comprehension = a way to create a new list with less syntax can mimic certain lambda functions, easier to read
#                       list = [expression (if/else)for item in itearable]

squares = []

for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

#passed_students = list(filter(lambda x: x >= 60, students))

#passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)


# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

#-------------------------------------------------------------------

cities_in_F = {'New york':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/6)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York': "showing", 'Boston': "Sunny", "Los angles":"sunny", "Chicago":"cloudy"}
sunny_weather = {key: value for  (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

cities = {'New york':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 60 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New york':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)

#zip(iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                 creates azip object with paired wlements stored in tuples for each elements

usernames = ["Dude", "Bro", "Mister"]
passwords = ('p@assword', "abc123", "guest")
login_date = ["1/1/23", "1/1/2021", "1/3/2021"]

users = dict(zip(usernames, passwords))
print(users)
print(type(users))

for key, value in users.items():
    print(key+":" +value)

#---------------------
users = zip(usernames, passwords,login_date)

for i in users:
    print(i)


# time module

import time

print(time.ctime(0))  # convert a time in seconds since epoch to a readable string
#                     epoch = when your computer thinks time began (reference point)

print(time.time())  # return current seconds since epoch
print(time.ctime((time.time())))  # will get current time

# --------------------------------------------------------------------------------------

time_object = time.localtime()  # local time
print(time_object)
#time.strftime # formats a time_obj3ect to string
time_object = time.gmtime()  # UTC time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)




# (year, month,  day, hours, minutes, secs, # day of the week, # day of the year
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.asctime(time_tuple)
print(time_string)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.mktime(time_tuple)
print(time_string)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)


# thread  = a flow of execution, like a separate order of instructions, however each thread takes a turn
#              runing to achieve concurrency

#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the python interpeter  at any one time


# cpu bound = program/task spends most of its time waiting for internal events  (CPU intensive)
#               use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web sracping)
#                use multithreading



import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffe():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You are studing")

eat_breakfast()
drink_coffe()
study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()


y = threading.Thread(target=drink_coffe, args=())
y.start()


z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

"""deamon thread = a thread  that runs in the background, not important for program to run
#                 your program will not not wait for daemon treads to complete  before existing
#                 non-daemon threads cannot normally be killed, stay alive until task is completed

#                  eg. background tasks, garbage collections, waiting for input, long running process


import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()
#x.setDaemon(True)
#print(x.isDaemon())

answer = input("Do you wish to exit?")




"""
