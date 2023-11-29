print("Welcome to the BMI machine calculation ")
person_height = float(input(' Height In meter: '))
person_weight = int(input("In kilograms: "))
# your BMI calculation
bmi = person_weight / (person_height * person_height)
if bmi < 18.5:
    print(f"Your BMI is {bmi} ........... you are under weight...")
elif bmi < 25:
    print(f"Your BMI is {bmi} ........... you are a normal weight...")
elif bmi < 30:
    print(f"Your BMI is {bmi} ........... you are slightly over weight...")
elif bmi < 35:
    print(f"Your BMI is {bmi} ........... you are Obese weight...")
else:
    print(f"Your BMI is {bmi} ........... you are clinicaly obses weight...")