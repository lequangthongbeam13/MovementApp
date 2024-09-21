# THIS FILE IS ONLY w2 TASK

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
print (Bday)
# Asking Age and Name
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

    # Detected
    List = ['Y','N']
    Choice = random.choice(List)
    if Choice == 'Y':
        print("Movement Detected")
    else:
        print("Movement not Detected")   

