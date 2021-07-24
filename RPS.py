import random

li = ["stone" , "paper" , "scissors"]
game = li

while True:
  system = random.choice(game)

  def result():
   return print(f"Ahh you won .... I choose {system}")

  player = input("lets play.... choose your choice \n")

  if system == player:
   print(f"Ahh its a draw... I choosed {system} too")

  elif system == "stone" and player == "paper":
   result()

  elif system == "paper" and player == "scissors":
   result()

  elif system == "scissors" and player == "stone":
   result()

  elif player not in li:
   print("Proper spelling bro atleast")

  else:
   print(f"You lose I choose {system}")
