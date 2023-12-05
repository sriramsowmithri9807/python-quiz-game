print("Welcome to my quiz game!!!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
    print("Okay! Let's Play :) ")
score = 0

answer = input("what you do when you are alone? ")
if answer == "i read books":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what you do when you are confused? ")
if answer == "i will be silent!":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score ) + "questions correct!")
print("You got " + str((score/2) * 100) + "%.")
