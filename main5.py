import json
import string
import random
import requests
import pandas as pd
import matplotlib.pyplot as plt

Name = ""
PassWord = ""
# MENU THINGS
def AskMenu(): 
    MenuChoose = input("Choose your option: ")
    return MenuChoose
def NavigateMenu():
    while True: 
        choice = AskMenu()
        if choice == "2":
            result = CreateNewAcc()
            if result == "back":
                return  # Back to main menu
            else:
                PasswordGenerator()
                UpdateInformation()
        elif choice == "3":
            print("See You Next Time!")
            exit()
        elif choice == "1":
            result = LoginUser()
            if result == "back":
                return  # Quay lại menu chính
        else:
            print("\nPlease choose correct option in MENU")
# MENU 2
def Menu2():
    print ("\nChoose option from Menu below:")
    print("1. See your information")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Show CPU Temperature and Motion Dectector Values")
    print("4. Guessing Game")
    print("5. Go Back From Beginning")
    print("6. Exit")
    NevigateMenu2()
    return None
def NevigateMenu2():
    while True:
        Choice2 = AskMenu()
        if Choice2 == "6":
            print("See You Next Time!")
            exit()
        elif Choice2 == "5":
            main()
        elif Choice2 == "4":
            GuessingGame()
        elif Choice2 == "3":
            TempAndMotionValues()
        elif Choice2 == "1":
            print("User Information")
        else:
            print("Please Choose correct option")
            print ("\nChoose option from Menu below:")
            print("1. See your information")
            print("2. Convert Celsius to Fahrenheit")
            print("3. Show CPU Temperature and Motion Dectector Values")
            print("4. Guessing Game")
            print("5. Go Back From Beginning")
            print("6. Exit")
            NevigateMenu2()

        return None

def TempAndMotionValues():
    url ="https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    data = response.json()

    for entry in data["feeds"]:
        print("")
        movement_value = entry ["field1"]
        temp_value = entry["field2"]
        time_value = entry["created_at"]
        if movement_value == "1":
            print(f"Movement detected: YES")
        elif movement_value == "0":
            print(f"Movement detected: NO")
        #print(f"Motion value: {movement_value}")
        print(f"Temperature value: {temp_value}°C")
        print(f"Date: {time_value[0:10]}")
        print(f"Time: {time_value[11:19]}")
    Menu3()
def Menu3():
    print ("\nChoose from Menu below:")
    print ("1. Show Graph")
    print ("2. Go Back")
    print ("3. Exit")
    NevigateMenu3()
def NevigateMenu3():
    while True:
        Choice3 = AskMenu()
        if Choice3 == "1":
            ShowGraph()
            Menu2()
        elif Choice3 == "2":
            Menu2()
        elif Choice3 == "3":
            print("See You Next Time!")
        else:
            print("Please Choose correct option")
            print ("\nChoose from Menu below:")
            print ("1. Show Graph")
            print ("2. Go Back")
            print ("3. Exit")
        return Choice3



def ShowGraph():
    UTemperatue = []
    UMovement=[]
    url ="https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    data = response.json()
    for entry in data["feeds"]:
        movement_value = entry ["field1"]
        temp_value = entry["field2"]
        # time_value = entry["created_at"]
        UTemperatue.append(temp_value)
        UMovement.append(movement_value)
        # print(f"Movement value: {movement_value}")
        # print(f"Temperature value: {temp_value}")
        # print(f"At: {time_value}")
    data = {
        'Temperature': UTemperatue,
        'Movement': UMovement
        }
    df = pd.DataFrame(data)
    print (df.to_string(index =False))
    # df.set_index('Temperature', inplace=True)
    # print (df)
    # Example data
    data = {
    'Temperature': UTemperatue,
    'Movement': UMovement
    }
    # Create DataFrame
    df = pd.DataFrame(data)
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(df['Temperature'], label='Temperature')
    plt.plot(df['Movement'], label='Movement')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Temperature and Movement Over Time')
    plt.legend()
    plt.show()

# CREATE NEW ACC
def CreateNewAcc():
    global Name
    print("\nHello new User!")
    print("- Enter (1) to Go Back.")
    print("- Or you can enter your first name to create new account.")
    Fi = str(input("Enter your first name: "))
    if Fi == "1":
        return "back"  # Turn back to main menu
    else:
        La = str(input("Enter your last name: "))
        print("\nEnter your Birthday")
        # Xử lý nhập ngày, tháng, năm như hiện tại
        while True: 
            try: 
                Day = input("Day(dd): ")
                if int(Day) > 31 or int(Day) < 1 or len(Day) != 2:
                    print("Invalid day. Try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        while True: 
            try: 
                Month = input("Month(mm): ")
                if int(Month) > 12 or int(Month) < 1 or len(Month) != 2:
                    print("Invalid month. Try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        while True: 
            try: 
                Year = input("Year(yyyy): ")
                if int(Year) >= 2025 or len(Year) != 4:
                    print("Invalid year. Try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        Bday = Year + Month + Day
        Name = Fi + " " + La
        print(f"Hello {Fi} {La}, welcome to the Motion Detector!")
        print(f"Your Username is: {Fi[0:2]}{La[0:3]}{Bday}")
        return None
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
    main()
# LOGIN THINGS
def ReadData():
    with open ("/Users/beam/Documents/BEAM /Cá Nhân Beam/LAB SE 1/Programming /MovementApp/MovementApp/data.json", "r") as file:
        data = json.load(file)
        return data
def LoginUser():
    print("\nWelcome back!")
    NameLogIn = input("Enter your name or\n(1) to Go Back: ")
    if NameLogIn == "1":
        return "back"
    else:
        PassLogIn = input("Enter your password: ")
        data = ReadData()
        users = data.get("users", [])
        for user in users:
            if user.get("name") == NameLogIn and user.get("password") == PassLogIn:
                print("Login successful!")
                print(f"\nWelcome, {user['name']}")
                print(f"You have the {user['rights']}.")
                if user['rights'] == "Admin Rights":
                    AdminMenu()  # Gọi menu dành cho admin
                else:
                    Menu2()  # Gọi menu người dùng
                return NameLogIn
        print("\nLogin failed. Incorrect username or password.")
        return "back"
#Admin Menu
def AdminMenu():
    print("\nAdmin Menu:")
    print("1. View all users")
    print("2. Delete a user")
    print("3. Normal Menu")
    print("4. Go back to main menu")
    choice = input("Choose your option: ")
    if choice == "1":
        ViewAllUsers()
    elif choice == "2":
        DeleteUser()
    elif choice == "3":
        Menu2()
    elif choice == "4":
        main()
    else:
        print("Invalid choice! Please try again.")
        AdminMenu()
#view List of Users
def ViewAllUsers():
    data = ReadData()
    users = data.get("users", [])
    print("\nList of all users:")
    for user in users:
        print(f"Name: {user['name']}, Rights: {user['rights']}")
    print("\nPress (1) to go back to Admin Menu.")
    choice = input("Your choice: ")
    if choice == "1":
        AdminMenu()  # back to Admin Menu
    else:
        print("Invalid choice! Please try again.")
        ViewAllUsers()
#Delete User
def DeleteUser():
    data = ReadData()
    users = data.get("users", [])
    print("\nList of users:")
    for i, user in enumerate(users):
        print(f"{i+1}. {user['name']} - {user['rights']}")
    choice = input("Enter the number of the user you want to delete (or 0 to cancel): ")
    if choice == "0":
        AdminMenu()
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(users):
                del users[index]
                with open("/Users/beam/Documents/BEAM /Cá Nhân Beam/LAB SE 1/Programming /MovementApp/MovementApp/data.json", "w") as file:
                    json.dump({"users": users}, file, indent=4)
                print("User deleted successfully!")
                AdminMenu()

            else:
                print("Invalid choice! Please try again.")
                DeleteUser()
        except ValueError:
            print("Invalid input! Please try again.")
            DeleteUser()
scoreboard = []

def GuessingGame():
    print("\nWelcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100 within 8 rounds.")
    print("You can type 'quit' anytime to exit the game.")
    
    while True:
        secret_number = random.randint(1, 10)  # Chọn số ngẫu nhiên
        attempts = 0
        max_attempts = 5
        print("\nA new game has started!")
        
        while attempts < max_attempts:
            user_input = input(f"Round {attempts + 1}/{max_attempts} - Your guess: ")
            
            # Kiểm tra nếu người dùng muốn thoát
            if user_input.lower() == "quit":
                print("You have exited the game.")
                Menu2()
            
            # Kiểm tra đầu vào
            try:
                guess = int(user_input)
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 10.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
            # So sánh đoán với số bí mật
            attempts += 1
            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                scoreboard.append(f"Game {len(scoreboard) + 1}: Won in {attempts} rounds")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        # Kết quả khi hết số lượt đoán
        if attempts == max_attempts and guess != secret_number:
            print(f"Sorry, you've used all {max_attempts} rounds. The correct number was {secret_number}.")
            scoreboard.append(f"Game {len(scoreboard) + 1}: Lost")
        
        # Hiển thị bảng điểm
        print("\nScoreboard:")
        for score in scoreboard:
            print(score)
        
        # Hỏi người chơi có muốn chơi lại không
        play_again = input("Do you want to play again? (yes to continue, quit to exit): ").lower()
        if play_again == "quit":
            print("Thank you for playing! Goodbye!")
            Menu2()
# Final main function
def main():
   while True:
        print("\n******************************")
        print("* Welcome To Motion Detector *")
        print("******************************")
        print("1. Login")
        print("2. Create a new account")
        print("3. Exit")
        NavigateMenu()

main()

