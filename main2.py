import json
import string
import random
Name = ""
PassWord = ""
# MENU THINGS
def AskMenu(): 
    MenuChoose = input("Choose your option: ")
    return MenuChoose
def NavigateMenu():
    choice = AskMenu()
    if choice  == "2":
        CreateNewAcc()
        PasswordGenerator()
        UpdateInformation()
    elif choice == "3":
        print("See You Next Time!")
    elif choice == "1":
        LoginUser()
    return None
# MENU 2
def Menu2():
    print ("\nChoose option from Menu:")
    print("1. See your information")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Show  CPU Temperature")
    print("4. Show  Motion Information")
    print("5. Guessing Game")
    print("6. Exit")


# CREATE NEW ACC
def CreateNewAcc():
    global Name
    print("\nHello new User!")
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
    Name = Fi + " " + La
    print(f"Hello {Fi} {La}, welcome to the Motion Detector!\nLet's Start!!!\nYour Username is: {Fi[0:2]}{La[0:3]}{Bday}")
    return Name
def PasswordGenerator():
    global PassWord
    # Passwords Generator           
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
        Num.append(random.choice(["0","1","2","3","4","5","6","7","8","9"]))


    # Special characters
    while len(Special) <= (SpecialUser-1):
        Special.append(random.choice(string.punctuation))
    
    PassWordCombine = "".join(UpperCase+LowerCase+Num+Special)
    charPassWord = list(PassWordCombine)
    random.shuffle(charPassWord)
    PassWord = "".join(charPassWord)

    print(f"\nYour password is: {PassWord} ")
    # print ("\nYour password is: ",*UpperCase, *LowerCase,*Num,*Special, sep="")

    # Asking HAPPY??
    Happy = input("Are you happy with this Password? (y/n): ")

    if Happy == "n":
        while Happy == "n":
            PassWordCombine = ''.join((random.choice(string.ascii_uppercase) for i in range(UpUser))) + ''.join((random.choice(string.ascii_lowercase) for i in range(LowUser)))+ ''.join((random.choice(string.digits) for i in range(NumberUser))) + ''.join((random.choice(string.punctuation) for i in range(SpecialUser)))
            charPassWord = list(PassWordCombine)
            random.shuffle(charPassWord)
            PassWord = "".join(charPassWord)
            print (f"\nYour new password is: {PassWord}")
            Happy = input("Are you happy with this Password? (y/n): ")
            print (f"\nOKE, your final password is: {PassWord}")
    elif Happy == "y":
        print (f"\nOKE, your fianal password is:{PassWord}")
def UpdateInformation():
    global Name
    global PassWord
    # New user data to be added
    new_user= {"name": f"{Name}", "password": f"{PassWord}","rights": "User Rights"}
    # Reading the existing data from the JSON file
    with open("/Users/beam/Documents/BEAM /Cá Nhân Beam/LAB SE 1/Programming /MovementApp/MovementApp/data.json", "r") as file:
        data = json.load(file)
    # Adding the new user to the list of users
    data["users"].append(new_user)
    # Writing the updated data back to the JSON file
    with open("/Users/beam/Documents/BEAM /Cá Nhân Beam/LAB SE 1/Programming /MovementApp/MovementApp/data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Updated data written to data.json")
# LOG IN THINGS
def ReadData():
    with open ("data.json", "r") as file:
        data = json.load(file)
        return data
def LoginUser():
    print("\nWelcome back!")
    NameLogIn = input("Enter your name: ")
    PassLogIn = input("Enter your password: ")
    data = ReadData()
    users = data.get("users",[])
    for user in users:
        if user.get("name") == NameLogIn and user.get("password") == PassLogIn:
            print("Login successful!")
            print(f"\nWelcome, {user['name']}")
            print(f"You have the {user['rights']}.")
            return
    print("\nLogin failed. Incorrect username or password.")
    print("\n1. Try again")
    print("2. Create a new account")
    print("3. Exit")
    NavigateMenu()
    



    
    return None
# Final main function
def main():
    print("******************************")
    print("* Welcome To Motion Detector *")
    print("******************************")
    print("1. Login")
    print("2. Create a new account")
    print("3. Exit")
    NavigateMenu()
    Menu2()
    
    return None
    
main()





