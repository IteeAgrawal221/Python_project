print("welcome to my computer quiz!")

playing = input('do you want to play game? ')

if playing.lower() != 'yes':
    quit()
print("okay! let's play :)")

score = 0

answer = input("what does CPU stand for: ")
if answer.lower() == 'central processing unit':
    print("correct!")
    score += 1
else:
    print(" Incorrect!")

answer = input("What does GPU stands for: ")
if answer.lower() == 'graphics processing unit':
    print("correct!")
    score +=1
else:
    print(" Incorrect!")

answer = input("What does RAM stands for: ")
if answer.lower() == 'Random acess memory':
    print("correct!")
    score +=1
else:
    print(" Incorrect!")

answer = input("what does PSU stand for: ")
if answer.lower() == 'power supply':
    print("correct!")
    score +=1
else:
    print(" Incorrect!")

answer = input("who is the father of computer: ")
if answer.lower() == 'Charles Babbage':
    print("correct!")
    score +=1
else:
    print(" Incorrect!")

print("you got " + str(score) + " questions correct!")

print("you got " + str((score/5) * 100) + " %")