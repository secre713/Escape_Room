import subprocess

print("Welcome to the Escape Room!")
print("You find yourself locked in a room filled with mysterious puzzles.")
print("Your goal is to solve the puzzle")
print("select any of the following rooms \n1.Jumble Word\n2.Riddles\n3.Tic-Tac-Toe\n4.Guess the lyrics(Easy)\n5.Guess the lyrics(Hard)\n")
a = int(input('Select the room:'))
if a == 1:
    subprocess.run(["python", "Escape_Room_1.py"])
if a == 2:
    subprocess.run(["python", "Escape_Room_2.py"])
if a == 3:
    subprocess.run(["python", "Escape_Room_3.py"])
if a == 4:
    subprocess.run(["python", "Escape_Room_4.py"])
if a == 5:
    subprocess.run(["python", "Escape_Room_5.py"])