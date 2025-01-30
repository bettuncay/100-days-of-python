#Rock Paper Scissors
import random
Paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
Rock = """
    _______
---'   ____ )
      (_____)
      (_____)
      (____)
---.__(___)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [Rock,Paper,Scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
ben = game[choice]
print(ben)
computer = random.choice(game)
print("Computer chose:" + computer)

if ben == Rock and computer ==Rock:
    print("It's a tie!")
elif ben == Paper and computer == Paper:
    print("It's a tie!")
elif ben == Scissors and computer == Scissors:
    print("It's a tie!")
elif ben ==Rock and computer ==Scissors:
    print("You win!")
elif ben == Paper and computer == Rock:
    print("You win!")
elif ben ==Scissors and computer == Paper:
    print("You win!")
else:
    print("You lose.")    
    
    
