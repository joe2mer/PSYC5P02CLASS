# -*- coding: utf-8 -*-
# Lecture4.py
"""
these are some lecture notes for the 4th lecture 
"""

# editor is where we have our script 
# python script ends with py 
# to leave comments you use the # 

myvar = "hello world" #writing hello world to myvar

# need to leave him comments on our assignments 

# loop is an instruction that repeats until a specified condition is met

# two different types of loops:
    # "for" loop runs for a preset number of times 
    # a "while" loop that is repeated as long as the expression is true

for i in range(1,5):
    print(i)
  
# 0 through 10 will go 0 through 9? They are non inclusive 

for i in range(1,5):
    print("i am in the loop")
    print(i)

print("i am out of the loop")

# i is being assigned a value in the loop 

# you can also loop through a list

mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

# x takes the value of each item in the list 

mylist = ["apple", "banana", "cherry"]
for x in range(len(mylist)):
    print(mylist[x])

# "while" loop, loops through a set number of times while a conditional statement is true

i = 1
while i < 6:
    print(i)
    i += 1

# += take the current value and add something to it 
# if you are not careful you can get stuck in an infinite loop

#ctrl + c it will kill the running process

#break command can be used to exit a loop 

#continue command will skip remaining commands in the loop and move onto the next loop iteration 

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)
    
#scope refers to the region of the code in which a variable or resource is visible and accessible 

#if variables are declared within a while or for loop, their scope exists inside that loop and nothing above it - local scope 

#in a global scope, all entities are visible throughout the entire program 

#largest scope is built-in scope 

for i in range(0,5): 
    x = i 
    print(x)
    
print(i)
print(x)
    
# i is going to be a range froom 0 to 4

#python is limited, you can add packages 

import numpy 
numpy.sqrt(4)

#can change the name of the library 

import numpy as np

np.sqrt(4)

x = np.sqrt(4)

# float is a floating integer. Has a floating decimal point. Different from an integer 
# integer has no decimal point 

# you can specifiy sub packages within a package

from math import cos, pi
print('cos(pi) is', cos(pi))

# one of the most common libraries used will be the random library. Can use this to simulate data, randomizing stimuli 
# rng are tied to a seed. 

import random 
help(random)

print(random.randint(3,9))

print(random.getstate())

mystate = random.getstate()

random.seed(1)

random.randint(0,9)

# to move from one side to another use ctrl + arrow key

# functions - ways that you can reuse code to increase efficiency 

# functions can take arguments (inputs) and can return values (outputs)
# print is a function 

# def means to define variable

def nameprintfunc(name):
    print('the name is' + name)
    return name 

nameprintfunc()

nameprintfunc('joe')

# return will print the value of the variable to the terminal

def adderfunc(val):
    x = val + val 
    print(x)
    return(x)
    
adderfunc(2)

#scope applies to function 

x = adderfunc(2)

# you can have multiple arguments separated by a comma and can make some optional by setting a default value 

def adderfunc(val = 4):
    x = val + val 
    print(x)
    return(x)

adderfunc()

adderfunc(2)

def adderfunc(val1, val2 = 4):
    x = val1 + val2 
    return(x)

# val2 = 4 only exists if I do not input a value. If I input a number it overwrites it 

def adderfunc(val1, val2 = 4):
    x = val1 + val2 
    y = (val1 + val2) * 2
    return(x)

#lists are changeable, tuples are not 
# can make a help function with three triple quotes 

def adderfunc(val1, val2 = 4):
    """adds two numbers together 
    
    """
    x = val1 + val2 
    y = (val1 + val2) * 2
    return(x, y)

#classes are like functions that have data. they build flexibility into your code 

#create a class called car. can assign to that class two different things:
    #attributes which are data 
    #methods which are operations 
#can create multiple instances of the class 

class car: 
    
    def __init__(self, color='white'):
        self.speed = 0
        self.color = color 
        
    def drive(self):
        self.speed = self.speed + 1 
    
    def breaking(self):
        self.speed = self.speed - 1 

vw = car()
toyota = car('green')

carlist = [car() for x in range(0,5)]

carlist[2].color     

vw.speed

#can create classes in a separate file 