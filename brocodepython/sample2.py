# list - used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "pudding"]

food[0] = "sushi"
print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
# food.clear()

for x in food:
    print(x)

# 2D lists - a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)
print(food[0][0])
print(food[2][1])

# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")

# set - collection which is unordered, unindexed. No duplicate values

utensils = {"Fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
print(utensils)
utensils.remove("Fork")
print(utensils)
# utensils.clear()
dishes.update(utensils)
print(utensils)
dinner_table = utensils.union(dishes)
print(dinner_table)

print(dishes.difference(utensils))
print(dishes.intersection(utensils))

# for x in dinner_table:
#   print(x)

print(dishes)
print(utensils)

# dictionary - a changeable, unordered colection of uniquue key: value pairs fast because they use hashing, allow
#               us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'
            }

# print(capitals['Germany'])  #gives error
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, values in capitals.items():
    print(key, values)

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vehas'})
capitals.pop('China')
# capitals.clear()


# index operator [] = gives access to a sequence's element (str, list, tuples)
name = "bro Code"

if (name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)


# function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("you are " + str(age) + " years old")
    print("Have a nice day!")


hello("Archana", "Seelan", 25)


# return statement - functions send python values/objects  back to the caller,
#                     These vlues/objects are known as the function's return value

def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 9)
print(x)


# another method for return function
def multiply(number1, number2):
    result = number1 * number2
    return result


x = multiply(6, 9)
print(x)

"""keyword arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments
                  doesn't matter, unlike positional arguments. python knows the names of the arguments that our functions recives
"""


def hello(first, middle, last):
    print('Hello ' + first + " " + middle + " " + last)


hello(last="Seelan", middle="Sathiya", first="Archana")

# nested functions calls = function calls inside other function calls
#                           innermost function cells are resolved first
#                           returned value is used as argument for the next outer function
num = (input("Enter a whole positive number: "))
num = float(num)
num = abs(num)
num = round(num)
print(num)


print(round(abs(float(input("Enter a whole positive number: ")))))


# scope = the region that a variable is recoginzed a variable is only available from inside the region it is created
#          a global and locally scoped versions of a variable can be created

name = "Bro"  # global scope (available inside and outside function)

def display_name():
    name = "Code"         # local scope (available only inside this function)
    print(name)

display_name()
print(name)



# *args = parameter that will pack all arguments into a tuple useful to that a function can accept a varying amount
#          of arguments

def add(*stuff):
    sum = 0
    for i in stuff:
        sum += 1
    return sum

print(add(2, 4, 5, 5, 6, 7, 8))

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += 1
    return sum

print(add(2, 4 , 5 ,5 , 6 , 78, 8))


# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying
#              amount of keyword arguments

def hello(**kwargs):
    print("Hello" +kwargs['first'] + " " + kwargs['last'])

hello(first="Bro", middle="Dude", last="Code")


def hello(**kwargs):
   print("Hello", end="")
   for key,value in kwargs.items():
       print(value,end="")

hello(first="Bro", middle="Dude", last="Code")


# str.format()  = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal, item))
print("The {} jumped over the {}".format("dog", "moon"))
print("The {0} jumped over the {1}".format(animal, item))  #positional argument
print(f"The {animal} jumped over the {item}".format(animal="cow", item="moon"))  #keyword argument


name = "Bro"

print("hello, my name is {}". format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
num = 1000

print("The number pi is{:.2f}".format(number))
print("The number pi is{:,}".format(num))
print("The number pi is{:b}".format(num))
print("The number pi is{:o}".format(num))
print("The number pi is{:X}".format(num))
print("The number pi is{:E}".format(number))


#Random numbers

import random

x = random.randint(1, 6)
y = random.random()

mylist = ['rock', 'paper', 'scissors']
z = random.choice(mylist)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)

# exeception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("end of the statement")

#file detection
import os

path = "C:\\Users\\archanaseelan\\Desktop"

if os.path.exists(path):
    print("Thet location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")

else:
    print("That location doesn't exist!")


#read a file

try:
    with open('text.txt') as file:
        print(file.read())
except FileExistsError:
    print("That file  was not found :(")



#write a filw

text = "Yooooooooooo\n This is some text \nHave a good one!\n"

with open('text.txt', 'w') as file:
    file.write(text)

#append a file
text = "Have a nice day!"

with open('text.txt', 'a') as file:
    file.write(text)


# copyfile() = copies contents of a file
# copy() = copyfile() - permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and mosificatio times)

import shutil

shutil.copy('text.txt', 'copy.txt')

#move a file

import os

source = "folder"
destination = "C:\\Users\\archanaseelan\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is a file directory")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileExistsError:
    print(source+ "was not found")


# delete a file

import os

path = "copy.txt"
os.remove(path)

#advance method

import os
import shutil

path = "text.txt"

try:
    os.remove(path)   #deletes a file
    #os.rmdir(path)     # delete an empty directory
    #shutil.rmtree(path) #deletes an directory containing files
except FileExistsError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using function")
else:
    print(path+" was deleted")


# module = a file  containing python code. May contain function, classes, etc
# used with modular programming, which is to separate a program into parts

import messages
import messages as mg
from messages import hello, bye
from messages import * # this one is dangerous

hello()
bye()

help("modules")
