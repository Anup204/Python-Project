n1 = input("Name 1: ")
n2 = input("Name 2: ")
combine_name = n1+n2

lower_name = combine_name.lower()
t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')
first_name = t+r+u+e
# print(first_name)

l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')
second_name = l+o+v+e
# print(second_name)
score = int(str(first_name)+str(second_name))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
