# print("baby f")
# print('0----')
# print(' ||||')
# print('babyf' * 4)

# # variable declaration
# price = 20
# price = 40.5
# name = 'Aali aaye'
# print(price)
# print(name)

# # input
# name = input("what is your name:")
# print('Hi ' + name * 10)

# practice
# name = input("what is your name: ")
# color = input("what is your favorite color: ")
# print(name+' likes ' + color)

# year = input('Birth year:')
# int()
# float()
# bool()
# type() tells the type of variable
# age = 2022 - int(year)
# print(age)
# print(type(age))

# weight_pound = input('How much you weigh: ')
# weight_kg = float(weight_pound)/2.20462
# print(weight_kg)

# the below code will show mutiple line display like an email
# course='''
# hello meray chotay bhai ka naam baby f hai aur usse barhe ka
# naam aali aaye hai aur sabse ka naam choara hai
# '''
# print(course)


# course = 'Python for beginners'
# print(course[-1])  # negative index return from the last

# the below code will display value of string of 0 to 3
# course = 'Pythons for Beginners'
# print(course[0:3])

# the below code will display value of string of 1 to end
# course = 'Pythons for Beginners'
# print(course[1:])

# the below code will display value of string from start to character 5
# course = 'Pythons for Beginners'
# print(course[1:4])

# the below code will copy first string into another string variable
# course = 'Pythons for Beginners'
# another = course[:]
# print(another)

# # string practice
# first = 'wahaj'
# last = 'ali'
# the line below will only run when the value of variable is string
# message = first + ' [' + last + '] is a coder'
# # formatted string
# msg = f'{first} [{last}] is a coder'

# print(msg)

# finding length of the string len is a general function not only count number of letters but can also be use in list
# course = 'Python for Beginners'
# print(len(course))

# upper case and lower case not modify variable
# print(course.upper())
# print(course.lower())
# print(course)

# find a letter/letters in a variable and give index
# print(course.find('Beginners'))

# it will find the word and give you the result true if there is this word or false if it is not in the string
# print('Python' in course)

# replace a letter/letters in a variable and give index
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.replace('P', 'J'))

# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
# If the word contains a number or a symbol, the first letter after that will be converted to upper case
# print(course.title())

# integers
# if you divide a value with double slash (//) it will return an integer value
# import math
# print(10/4)
# print(10//4)

# # modulus
# print(10 % 3)

# # for power use double asterik **
# print(10**3)

# # augmented assigment
# x = 10
# x += 3
# print(x)

# # round of value we use round
# x = 3.3
# print(round(x))

# # absolute
# print(abs(-2.9))

# # we can use math module also for calculation for that you have include math module(library) below and you can learn its function on python.org which is its documentation

# print(math.ceil(2.1))
# print(math.floor(2.9))

# # if statement
# is_hot = False
# is_cold = True
# if is_hot:
#     print("it is a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("wear warm clothes")
# else:
#     print("Its a lovely day")
# print("Enjoy your day")
# price = 10000
# print(f"the value of price is : ${float(price)}")

# # AND: both(if check AND check: )
# # OR: at least one(if check OR check)
# # NOT bhi use hota

# # comparison operator same syntax as c++
# temperature = 30
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print("It is not a hot day")

# practice

# weight = input("Weight: ")
# i = input("(L)bs or (K)g:")
# if i == 'k' or i == "K":
#     print(f"Your weight is {int(weight)*2.205} in pounds")
# elif i == 'l' or i == 'L':
#     print(f"Your weight is {int(weight) * 0.4536} in kg")

# while condition
# i = 1
# while i <= 5:
#     print(i)
#     i = i+1
# print("Done")

# break statement


# secret_num = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('guess: '))
#     guess_count += 1
#     if guess == secret_num:
#         print('You win')
#         break
# else:
#     # this else is of while and work the same as if else this work when condition is fulfilled
#     print('Sorry you failed')

# state = '0'
# while state != "quit":
#     state = input()
#     if state == "start":
#         print("Car started... Ready to go!")
#     elif state == "stop":
#         print("Car stopped.")
#     else:
#         if state != "quit":
#             print("I dont understand that...")

# for loops
# the item will everytime holds 1 character from python
# for item in 'Python':
#     print(item)

# for loop with list of numbers or name etc
# for item in ['Mosh', "Hamdani", "Sara"]:
#     print(item)

# # for looop with range function different eexamples
# for item in range(10):
#     print(item)

# for item in range(2, 10):
#     print(item)

# for item in range(6, 10, 2):
#     print(item)

# nested loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# # practice
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:

#     for y in range(x, x+1):
#         print('x' * y)

# list
# names = ['John', 'Bob', 'Mosh', 'Sarah']
# print(names[0])
# print(names[-2])
# print(names[2:])
# print(names[:2])
# print(names[1:3])
# print(names[:])
# # iff we print  names then it will print all values in list

# # we can also modify list by doing the following
# names[0] = 'Baby f'
# print(names)

# # practice list
# list = [1, 4, 3, 2, 5, 8]
# max = list[0]
# for x in list:
#     if x > max:
#         max = x
# print(max)

# # 2_D list
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# print(matrix[0][1])
# # modify list
# matrix[0][1] = 20

# # use 2-d list in for loop
# for row in matrix:
#     for item in row:
#         print(item)

# list function
# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)

# # to insert at any point we use .insert funtion
# # below line will insert 10 on 0 index
# numbers.insert(0, 10)
# # remove value 5 from the list if it exist
# numbers.remove(5)
# print(numbers)

# # .clear clear the list and .pop will pop last element
# # numbers.pop()
# # numbers.clear()

# # .index provide with the index of value
# print(numbers.index(1))

# # for existence of a value we use "in"
# print(50 in numbers)

# # for counting of a paritcular value we use .count function
# numbers = [5, 2, 1, 5, 7, 4]
# print(numbers.count(5))
# # .sort sort the function
# numbers.sort()
# print(numbers)
# # now if we use .reverse it will give us the value indescending oreder
# numbers.sort()
# print(numbers)

# # .copy() copy the list to another variable
# numbers2 = numbers.copy()

# # tuples we cannot append ,remove or insert in tuple
# numbers = (1, 2, 3)
# # but .count and .index can be used
# numbers.count(1)
# numbers.index(2)
# # print can be done in the same way as list
# print(numbers[0])

# # we cannot mutate/change tuples so following lin wont work
# numbers[0] = 10

# unpacking
# the two ways below do the same thing but the latter one is only used in python to make it more efficient
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# x, y, z = coordinates
# print(x)
# # the above line is called unpacking and we can use this feature with list too.
# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(y)


# Dictionary we use curly brackets, key should be unique e.g cannot be two age
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# # the below line will not work because the key their has Capital 'N' instead of 'n'.
# # print(customer["Name"])

# # the key letters should be same as key in dictionary so to avoid error we use .get so if that key doesnt exist it will return none
# print(customer.get("birthdate"))
# # instead of getting none we can also use a default value
# print(customer.get("birthdate", "Jan 1 1980"))

# # we can update the values of key
# customer["name"] = "Jack Smith"
# print(customer["name"])
# # we can also add keys
# customer["birthdate"] = "Dec 6 2006"
# print(customer["birthdate"])

# practice
# phone = input("Phone: ")
# num = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero"
# }
# output = ""
# for x in phone:
#     output += num.get(x) + " "
# print(output)

# emoji converter
# message = input(">")
# # the line below will return a list as space work as delimiter
# words = message.split(' ')
# print(words)

# emojis = {
#     ":)": "😃",
#     ":(": "😟"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# function creation/defining
# def greet_user():
#     print("Hi there")
#     print('welcome aboard')


# print("Start")
# greet_user()
# print("Finish")
# parameters of functions


# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print("Welcome aboard")


# print("Start")
# greet_user("Aali", "Aaye")
# greet_user("Mary", "jane")
# print("Finish")

# keyword arguments we edefine which argument go where
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print("Welcome aboard")


# print("Start")
# greet_user(last_name="Aali", first_name="Aaye")
# print("Finish")

# return in function by default none is return by function
# def square(number):
#     return number * number


# print(square(3))

# def emoji_converter(message):
#     # the line below will return a list as space work as delimiter
#     words = message.split(' ')
#     # print(words)

#     emojis = {
#         ":)": "😃",
#         ":(": "😟"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input(">")
# print(emoji_converter(message))

# exception
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("Zero cant be an age")
# except ValueError:
#     print("invalid Value")


# CLASSES ,for classes variable we capitalise the first letter of every word
# self here is a pointer of that object


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# the below line is the way to identify an object of a class
# point1 = Point()
# the below line is the way to give variables to an object to a class
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
# the classes can attributes anywhere in program where they are defined like x and y.
# point2 = Point()
# point2.x = 3
# print(point2.x)

# the above line of attributes has issue if we hadnt identify an attribute oof an object than there will not be any attribute so we make constructor
# constructor made in Point class which is made through init
# point = Point(10, 20)
# point.x = 11
# print(point.x)

# practice
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'Hello my name is {self.name}')


# person = Person("Baby f")
# person.talk()

# person1 = Person("Aali Aaye")
# person1.talk()

# inheritance
# we use parenthesis for inheeritance, pass used to tell python decoder that its okay that its empty right now.
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")


# class Cat(Mammal):
#     pass


# dog1 = Dog()
# dog1.walk()
# dog1.bark()

# modules
# to just import 1 function we use below syntax
# from converters import lbs_to_kg
# import converters
# print(converters.kg_to_lbs(60))
# print(lbs_to_kg(100))

# import util
# numbers = [5, 32, 5, 6, 62, 3, 5, 3, 33, 44, 66, 55]
# print(util.find_max(numbers))
# print(max(numbers)) this comment line will give the same result as above as maxx is a built in function.

# packages
# packages are like directories where there are modules in that directory and below is the way to use packages
# import ecommerce.shipping

# ecommerce.shipping.calc_shipping()
# another way is using 'from'
# for multiple function we use ',' e.g from ecommerce.shipping import calc_shipping, calc_boarding
# from ecommerce.shipping import calc_shipping
# from ecommerce import shipping

# generate random numbers using random module
import random
# print(random.random())
# print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Lol']
# leader = random.choice(members)
# print(leader)

# practice
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second

#         # or tu=(first, second) and then return tu
# dice = Dice()
# print(dice.roll())

# working with directories
# absolute path and relative path
# we can make directory and delete directory
# this line is used for using path
from pathlib import Path
# path = Path("ecommerce1")
# print(path.rmdir())

# .glob is used to find or search current directory
path = Path()
print(path.glob('*.*'))
