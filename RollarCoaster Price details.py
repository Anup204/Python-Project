print("Welcome to the rollercoaster  ")
height = int(input("What is your height: "))
bill = 0
if height >= 120:
    print("Yes ...You can ride the rollercoaster!!")
    age = int(input("What is your age: "))
    if age < 12:
        print("You can ride")
        print("Please pay $6 ")
        bill = 6
    elif age <= 18:
        print("You can ride .....")
        print("$7")
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything going to be ok.. have free ride...")
    else:
        print("$12")
        bill = 12
    wants_photo = input("Do you want a photo taken Y or N....")
    if wants_photo == 'Y' or 'y' or 'yes' or 'Yes':
        #add bill 
        bill += 3
    print(f"The total cost {bill}$")
else:
    print("Sorry to say... grow taller than come again")