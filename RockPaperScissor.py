import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''


scissor = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock,paper,scissor]


print('What do you choose Type 0 for rock, 1 for paper, 2 for scissor')
user_input = int(input("Enter :"))
print("User choice")
print(game_image[user_input])


computer_input = random.randint(0,2)
print("Computer choice")
print(game_image[computer_input])

if user_input > 2:
    print("Srry.. invalid key.....You lose")
elif user_input == 0 and computer_input == 2:
    print("You win")
elif user_input == 2 and computer_input == 0:
    print("You Lose")
elif user_input == computer_input:
    print("Its draw")
elif user_input == 0 and computer_input == 1:
    print("You Lose")
elif user_input == 1 and computer_input == 0:
    print("You win")
elif user_input == 1 and computer_input == 2:
    print("You Lose")
elif user_input == 2 and computer_input == 1:
    print("You Win")