# Username Program
Fi = str(input("Enter your first name: "))
La = str(input("Enter your last name: "))
print("\nEnter your Birthday")
Day = input("Day(dd): ")
Month =input("Month(mm): ")
Year = input("Year(yyyy): ")
Bday = Year + Month + Day
print(f"Hello {Fi} {La}, welcome to the Motion Detector!\nLet's Start!!!\nYour Username is: {Fi[0:2]}{La[0:3]}{Bday}")
# Movement in room
input("\nHas there been movement in the room? (yes/no): ")
print("Movement detected: YES / NO")
# Calculate  Fahrenheit. 
Degree = float(input("\nEnter temperature in C°: "))
print(f"The given temperature {Degree}C° is {round(Degree*1.8+32,1)}F°.")




# input("Your first name: ")
# input("Your last name: ")
# from datetime import datetime
# birthday = input("Enter your date of birth: ")
# bday = datetime.strptime(birthday, '%d/%m/%Y')
# print (bday)