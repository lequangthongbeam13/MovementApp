# This file 'main.py' is the combination of w1 and w2.



# Username Program
Fi = str(input("Enter your first name: "))
La = str(input("Enter your last name: "))
print("\nEnter your Birthday")
# Formatted Day
while True: 
    try: 
        Day = (input("Day(dd): "))
        if (int(Day)) >= 32 or int(Day) == 0 or int(Day)< 0 or len(str(Day)) != 2:
            print("Wrong Formatted Date, please try again in right format(dd) and the number from 01 to 31")
            
        else:
            break
    except ValueError:
        print("That's not a number! Please try again")      
   
# Formatted Month
while True: 
    try: 
        Month =(input("Month(mm): "))
        if (int(Month)) >= 13 or int(Month) == 0 or int(Month)< 0 or len(str(Month)) != 2:
            print("Wrong Formatted, please try again in right format(mm)and the number from 01 to 12")
            
        else:
            break
    except ValueError:
        print("That's not a number! Please try again")
# Formatted Year
while True: 
    try: 
        Year =(input("Year(yyyy): "))
        if (int(Year)) >=2025 or len(str(Year)) != 4:
            print("Wrong Formatted, please try again in right format(yyyy and the number < 2025)")
            
        else:
            break
    except ValueError:
        print("That's not a number! Please try again")
Bday = Year + Month + Day
print(f"Hello {Fi} {La}, welcome to the Motion Detector!\nLet's Start!!!\nYour Username is: {Fi[0:2]}{La[0:3]}{Bday}")
# Movement in room
input("\nHas there been movement in the room? (yes/no): ")
print("Movement detected: YES / NO")
# Calculate  Fahrenheit. 
Degree = float(input("\nEnter temperature in C°: "))
print(f"The given temperature {Degree}C° is {round(Degree*1.8+32,1)}F°.")

# Asking Age and Name
#If User wirte 'quit' from the beginning of this part, the program will quit...

Q = "quit"
Name = input("Enter your name: ")
if Name == Q:
    print("Goodbye!")
else:
    if Name == "Beam Le":
        print(f"Welcome {Name}! You have the admin rights.")
    elif Name == "Mira":
        print(f"Welcome {Name}! You have SUPER-USER rights.")
    else:
        Age = input("Enter your age: ")
        if int(Age) >= 18:
            print(f"Welcome {Name}! You have viwer rights.")
        else:
            print(f"Greetings {Name}! You are too young to operate this program.")
    # Temperature
    import random
    while True:
            Temp = (random.randint(-20,100))
            TempInput = input("\nDo you want to see the temperature in C° or F°? (c/f): ")
            if TempInput == "c":
                if Temp >90:
                    print (f"The temperature of the CPU is {Temp} C°.ON FIRE!!!")
                elif Temp >80:
                    print (f"The temperature of the CPU is {Temp} C°.Too Hot!!!")
                else:
                    print (f"The temperature of the CPU is {Temp} C°.OK!")
                break
            elif TempInput == "f":
                if Temp>90 :
                    print (f"The temperature of the CPU is {round(Temp*1.8+32,1)} F°.ON FIRE!!!")
                elif Temp>80:
                    print (f"The temperature of the CPU is {round(Temp*1.8+32,1)} F°. TOO HOT!!")
                else:
                    print (f"The temperature of the CPU is {round(Temp*1.8+32,1)} F°.OK!")
                break
            elif TempInput != "c" or TempInput != "f":
                print ("Not valid!!! Please enter 'c' or 'f'")

    # Detected Movement
    List = ['Y','N']
    Choice = random.choice(List)
    if Choice == 'Y':
        print("Movement Detected")
    else:
        print("Movement not Detected")
# Passwords Generator           
import string
import random
# string.ascii_lowercase
# string.ascii_uppercase
# random. randint(0, 9)
# string.punctuation
print("\nPasswords Generator")
UpUser = int(input("Number of capital letters: "))
LowUser = int(input("Number of small letters: "))
NumberUser = int(input("Number of digits: "))
SpecialUser = int(input("Number of special characters: "))
# List of each character in Password
UpperCase = []
LowerCase = []
Num = []
Special = []


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


 


