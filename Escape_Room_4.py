score = 0

#Question1
print("Q1")
print("Find the missing lyrics:\n "
      "if you like your coffee hot\n"
      "let me be your coffee pot\n "
      "you call the shots babe\n"
      "_________________________")

missing_lyrics = input()
if (missing_lyrics == 'i wanna be yours'):
    print("correct ")
    score += 1
else:
    print("incorrect\n the correct answer is i wanna be yours")





#Question2
print("Q2")
print("so its gonna be forever\n"
          "or its gonna go down in flames\n"
          "you can tell me when its over\n"
          "its the high was worth the pain\n"
          "_____________________________\n")



missing_lyrics=input()
if(missing_lyrics=='got a long list of ex-lovers'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is got a long list of ex-lovers")




#Queation3
print("Q3")
print("the city's cold and empty \n"
      "no one's around to judge me\n"
      "__________________when you're gone\n")



missing_lyrics = input()
if (missing_lyrics == 'i cant see clearly'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is i cant see clearly")



#Question4
print("Q4")
print("we could've had it all\n"
      "rolling in the deep\n"
      "you had my heart inside of your hand\n "
      "and you played it ________________\n")



missing_lyrics = input()
if (missing_lyrics == 'to the beat'):
     print("correct")
     score += 1
else:
    print("incorrect\n the correct answer is to the beat")




#Question5
print("Q5")
print("Are we an item? (Yo) girl, quit playin\n" 
"We're just friends" "(yo), what are you sayin'\n?" 
"Said, There's another" "(yo), and looked right in my eyes \n"
"_________________________, and I was like \n"
"Baby, baby, baby, oh")


missing_lyrics = input()
if (missing_lyrics == 'My first love broke my heart for the first time'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is My first love broke my heart for the first time")


#Question6
print("Q6")
print("moving too fast,moon is lightin'up her skin\n"
      "she's falling,doesn't even know it yet\n"
      "having no regrets is _______________\n")


missing_lyrics = input()
if (missing_lyrics == 'all that she really wants'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is all that she really wants")




#Question7
print("Q7")
print("in your eyes,there's a heavy blue\n"
      "one to love,___________\n"
      "sweet devine,a heavy truth\n"
      "water or wine,don't make me choose\n")
missing_lyrics = input()
if (missing_lyrics == 'and one to lose'):
    print("correct")
    score += 1
else:
    print("incorrect\n the correct answer is and one to lose")
    print("Your Score is: ", score)
    if (score >= 4):
        print("congrats! you have escaped the room")
    else:
        print("you have failed to escape the room")



