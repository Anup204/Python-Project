year = int(input("enter a year....: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"{year} Leap year")
        else:
            print(f"{year} Not leap year")
    else:
        print(f"{year} Not leap year")
else:
    print(f"{year} Not leap year")
























year = int(input("enter a year....: "))
if year % 4 == 0:
    print(f"{year} Leap year")
elif year % 100 == 0:
    print(f"{year} Leap year")
elif year % 400 == 0:
    print(f"{year} Leap year")
else:
    print(f"{year} Not leap year")