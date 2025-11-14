score = 0

#Question1
print("Q1")
print("Who says, who says you're not perfect?\n"
"Who says you're not worth it?\n"
"Who says __________________________?")


missing_lyrics = input()
if (missing_lyrics == "you're the only one that's hurting"):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is you're the only one that's hurting")





#Question2
print("Q2")
print("Ladies and gentlemen, will you please stand?\n"
"With every guitar string scar on my hand\n"
"I take this magnetic force of a man to be my lover\n"
"My heart's been borrowed and yours has been blue\n"
"All's well that ends well to end up with you\n"
"Swear to be overdramatic and true to my lover\n"
"And ___________________________________________\n"
"And at every table, I'll save you a seat, lover")



missing_lyrics=input()
if(missing_lyrics=="you'll save all your dirtiest jokes for me"):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is you'll save all your dirtiest jokes for me")



#Queation3
print("Q3")
print("Yeah, breakfast at Tiffany's and bottles of bubbles\n"
"Girls with tattoos who like getting in trouble\n"
"______________________________________________\n"
"Buy myself all of my favorite things")


missing_lyrics = input()
if (missing_lyrics == 'lashes and diamonds, atm machines'):
    print("correct")
    score += 1

else:
    print("incorrect\n the correct answer is lashes and diamonds, atm machines")




#Question4
print("Q4")
print("Just to burn away their sorrows\n"
"________________________________\n"
"Just to tear down all their morals\n"
"And all is fair in love and war, she's pure")



missing_lyrics = input()
if (missing_lyrics == "I'll stay up till tomorrow"):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is I'll stay up till tomorrow")




#Question5
print("Q5")
print("think i'll miss you forever\n"
      "like the _________________________\n"
      "later's better than never\n"
      "even if you're gone,i'm gonna drive")



missing_lyrics = input()
if (missing_lyrics == 'stars miss the sun in the morning sky'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is stars miss the sun in the morning sky")




#Question6
print("Q6")
print("People say we shouldn't be together\n"
"We're ___________________________________\n"
"But I say,They don't know\n"
"What they're talk-, talk-, talking about" )


missing_lyrics = input()
if (missing_lyrics == 'too young to know about forever'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is too young to know about forever")




#Question7
print("Q7")
print("in your eyes,there's a heavy blue\n"
      "one to love,and one to lose\n"
      "___________,a heavy truth\n"
      "water or wine,don't make me choose")

missing_lyrics = input()
if (missing_lyrics == 'sweet devine'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is sweet devine")
    print("Your Score is: ", score)
    if (score >= 4):
        print("congrats! you have escaped the room")
    else:
        print("you have failed to escape the room")
