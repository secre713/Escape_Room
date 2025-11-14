score = 0

#Riddle1
print("welcome to the room 2 solve riddles to escape")
print("The more you take,the more you leave behind what am I?")
Answer=input()
if (Answer == 'footsteps'):
    print("correct")
    score += 1
else:
      print("incorrect\n the correct answer is footsteps")


# Riddle2
print("What goes down up but never comes down ?")
Answer = input()
if (Answer == 'age'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is age")


# Riddle3
print("I come from a mine and get surrounded by wood always,everyone uses me,who am i?")
Answer = input()
if (Answer == 'pencil lead'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is pencil lead")


# Riddle4
print("What dissappears as soon as you name it ?")
Answer = input()
if (Answer == 'silence'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is silence")


# Riddle5
print("What can you catch, but not throw? ")
Answer = input()
if (Answer == 'cold'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is cold")


# Riddle6
print("What four letter word can be written forward,backword or upside down but can still be read from left to right?")
Answer = input()
if (Answer == 'noon'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is noon")


# Riddle7
score = 0
print("A pizza place has an offer where you can swap five empty boxes for a free pizza.joe has collected 25 pizza boxes how many free pizzas can he get?")
Answer = input()


if (Answer == '6'):

    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is six")


# Riddle8
print("What has one eye, but can’t see?")
Answer = input()
if (Answer == 'needle'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is needle")


#Riddle9
print("This belongs to you, but everyone else uses it.")
Answer = input()
if (Answer == 'your name'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is your name")

# Riddle10
    print("What comes once in a minute, twice in a moment, but never in a thousand years?")
    Answer = input()
    if (Answer == 'the letter m'):
        print("correct")
        score += 1
    else:
        print("incorrect\n the correct answer is the letter m ")
        print("Your Score is: ", score)
if (score >= 4):
     print("congrats! you have escaped the room")
else:
    print("you have failed to escape the room")

