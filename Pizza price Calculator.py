print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input("Add pepperoni Y | N") # Do you want pepperoni? Y or N
extra_cheese = input("Add extra cheese Y | N") # Do you want extra cheese? Y or N

bill = 0
if size == 'S':
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
    if extra_cheese == 'Y':
      bill += 1
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == 'Y':
      bill += 1
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
else:
  print("We are waiting for order.....")

print(f"The total {bill}$ .")
