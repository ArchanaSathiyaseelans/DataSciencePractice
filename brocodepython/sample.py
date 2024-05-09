import math
import time

print("I love pizza")


#variable
name = "Bro"
print(type(name))
print("Hello " +name)

height=10.8
weight = 12
print(height + weight)

"""Multiple assignment = allows us to assign multiple variables at the same time in one line of code"""

name, age, attractive = "Bro", 21, True

print(name)
print(age)
print(attractive)

spongebob = patrick = Sandy = Squidward = 30

print(spongebob)
print(patrick)
print(Sandy)
print(Squidward)


"""String methods"""

name = "Bro code" #yes space counts but does not print space

print(len(name))
print(name.find("o"))
#print(name.index(2))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o", "a"))
print(name*3)


#type casting = connvert the dta type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #string

x = float(x)
y = str(y)
z = int(z)

print(x)
print(y)
print(z)


"""User input"""

#name = input("What is your name: ")
#age = int(input("How old are you: "))
#height = float(input("how tall are you: "))

#print("Hello " +name)
#print("You are " +str(age)+ " years old")
#print("you are "  +str(height)+" cm tall")


"""Math functions"""
pi = -3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 6))
print(math.sqrt(420)) # negative number will not work
print(max(x, y, z))
print(min(x, y, z))

"""String slicing"""
first_name = name[:3]
last_name = name[4:]
funky_name = name[::2] #[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slicing

website1 = "http://google.com"
website2 = "http://wikiipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])



"""if statement - a block of code that will execute if its condition is true """

age = int(input("How  old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child")


# logical operators (and, or, not) = used to check two or more conditional statements is true

temp = int(input("What is the temperature outside: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("go outside")
elif not(temp < 0 or temp >30):
    print("The temperatue is bad today!")
    print("stay inside")


# while loop - a statement that will execute it's block of code,
#                as long as its condition remains true


name = ""
while len(name) == 0:
    name = input("Enter your name!")

print("Hello" +name)


#another method
name = None
while not name:
    name = input("Enter your name!")

print("Hello" +name)

"""for loop - a statement that will execute it's block of code a limited amount of times"""
#                  while loop = unlimited
#                  For loop = limited

for i in range(10):
    print(1+1)

for i in range(50, 100+1, 2): #even numbers
    print(i)

for i in "Bro code":
    print(i)


for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")


# nested loops - The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


# loop control statements - change a loops execution from its normal sequence

# break - used to terminate the loop entirely
# continue - skips to the next iteration of the loop
# pass - does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


for i in range(1, 21):

    if i == 13:
        pass
    else:
        print(i)









