import string
import random
# string.ascii_lowercase
# string.ascii_uppercase
# random. randint(0, 9)
# string.punctuation
UpUser = int(input("Number of capital letters: "))
LowUser = int(input("Number of small letters: "))
NumberUser = int(input("Number of digits: "))
SpecialUser = int(input("Number of special characters: "))
# List of each character in Password
UpperCase = []
LowerCase = []
Num = []
Special = []

# Using while loop
# UpperCase
while len(UpperCase) <= (UpUser-1):
    UpperCase.append(random.choice(string.ascii_uppercase))


# LowerCase
while len(LowerCase) <= (LowUser-1):
    LowerCase.append(random.choice(string.ascii_lowercase))


# Number
while len(Num) <= (NumberUser-1):
    Num.append(random. randint(0, 9))


# Special characters
while len(Special) <= (SpecialUser-1):
    Special.append(random.choice(string.punctuation))

print ("\nYour password is: ",*UpperCase, *LowerCase,*Num,*Special, sep="")


# Trying to use for loop
# Asking HAPPY??
Happy = input("Are you happy with this Password? (y/n): ")

if Happy == "n":
    while Happy == "n":
        Pass = ''.join((random.choice(string.ascii_uppercase) for i in range(UpUser))) + ''.join((random.choice(string.ascii_lowercase) for i in range(LowUser)))+ ''.join((random.choice(string.digits) for i in range(NumberUser))) + ''.join((random.choice(string.punctuation) for i in range(SpecialUser)))
        print (f"\nYour new password is: {Pass}")
        Happy = input("Are you happy with this Password? (y/n): ")
        print (f"\nOKE, your final password is: {Pass}")
elif Happy == "y":
    print ("\nOKE, your fianal password is: ",*UpperCase, *LowerCase,*Num,*Special, sep="")


 