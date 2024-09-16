# ## this program is my first one
# print ("This is my first program.")
# ## Always comment your code!!!!

# print ("This is my second")
# print ("This is my") 

## single, and double qutations. And baclslashes.
# print ('He said: "Hello world" and keep trying...')
# print ("He said: \"Hello world\" and keep trying...")
# print("He said: \"Hello world\" \n \n \n \n \n \n \n  and keep trying...")

## Input:
# input ("What is your name?")
#print ("Welcome "+ input ("What is your name?") + "!")

## Choose words
#print ("Heloo"[0])
#print ("Heloo"[0:3])
#print ("123" +" 456" + " Hello" [0:3])

## Variable:
# Firstname = input("What is your first name?: " )
# print (Firstname)

##Substrings
# Sentence = "Fiding a substring."
# print (Sentence[-2])
# print (Sentence[9])
# print (Sentence[::2]) 
# print (Sentence[::4])
# print (Sentence[2:9:3]) # start from 0, take leter 2 to before 9, take every third one.
# print (Sentence[-9:-2])
# print (Sentence[::-2])

# #Data type:
# #Interger, whole number
# #Float
# print (3.14)

# Calclen = len("Calculate the number of characters")
#     print (Calclen)
# print (type(Calclen))

# Num1 = float(10)
# print (type(Num1))

# Num1 = int("20")
# Num3 = 30 + Num1
# print (Num3 + Num1)

from operator import mod
# print (mod(7/2))
# print(5 * 3 - 4 / 2 + 2)
# print(5 * 3 - 4 / (2 + 2))

# print (8/3)
# print (int(8/3))
# print (round(8/3))
# print (round(8/3,2))
# print (round(8/3,2))

##String formatting, Placeholders.

# Name = "Beam"
# Age = 10.123
# FormattedString = "My name is %s and I %f years old." % (Name, Age)
# print (FormattedString)

# Name = "Beam"
# Age = 10.123
# FormattedString = "My name is {0} and I {1} years old." .format (Name, Age)
# AnotherF = "Hi, am {0}"
# print (FormattedString)
# print (AnotherF)

# Name = "Beam"
# Age = 10123
# Number = int(round(8/3,2))

# FormattedString = "My name is %s and I am %d years old. And the number is %f" % (Name, Age,Number)
# print (FormattedString)

# EasyCalc = 0
# EasyCalc +=1
# EasyCalc -=1
# EasyCalc *=1
# EasyCalc /=1
# print (f"This is the result of easycalc:{EasyCalc}. Good job!")

import math
Radius = float(input ("Enter Cylinder Radius: "))
Height = float(input ("Enter Cylinder Height: "))
Volume = float(round(((math.pi) * Radius**2*Height),2))
# print("Your Cylinder Volume is %f" % Volume)
print(f"Your Cylinder Volume is: {Volume}")


