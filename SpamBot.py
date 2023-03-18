#yield statement suspends a functions's execution and sends a value back to the caller,
#but retains enough state to enable the function to resume where it left off.
#when the function resumes, it continues execution immediately after the last yield run.
#This allows its code to produce a series aof values over time, rather than computing them 
#at once  and sending them back like a list.

"""The self
Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, we still have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) this is all the special self is about.
"""
import random
import time
import pyautogui as pt
time.sleep(5)
file=open("compliment.txt", 'r')
file=list(file)

random.shuffle(file)

for word in file:
    time.sleep(0)
    pt.typewrite(word)
    pt.press("enter")




# Class or Static VariableYou can have the last bite.
# May I have this dance?s in Python:
# All objects share class or static variables. An instance or non-static variables are different for different objects (every object has a copy). For example, let a Computer Science Student be represented by a class CSStudent. The class may have a static variable whose value is “cse” for all objects. And class may also have non-static members like name and roll.
#  In C++ and Java, we can use static keywords to make a variable a class variable. The variables which don’t have a preceding static keyword are instance variables. See this for the Java example and this for the C++ example.

# Features of Static Variables
# Static variables are allocated memory ones when the object for the class is created for the first time.
# Static variables are created outside of methods but inside a class
# Static variables can be accessed through a class but not directly with a instance.
# Static variables behavior doesn’t change for every object.
# The Python approach is simple; it doesn’t require a static keyword. 

# Note: All variables which are assigned a value in the class declaration are class variables. And variables that are assigned values inside methods are instance variables.
