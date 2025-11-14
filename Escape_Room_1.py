import random

WORDS = ("migration", "microscope", "photosynthesis", "astronaut", "mitochondria","serendipity")

word = random.choice(WORDS)
correct = word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print ("Welcome to Word Jumble!")
print ("The jumble is:", jumble)

guess = input("Your guess: ")
guess = guess.lower()
while (guess != correct) and (guess != ""):
    print ("Sorry, wrong answer.")
    guess = input("Your guess: ")
    guess = guess.lower()

if guess == correct:
    print ("That's it!  You guessed it!\n")

print ("congrats! you have escaped the room")

exit = input("Press the enter key to exit.")
