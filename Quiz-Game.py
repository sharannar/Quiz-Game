print("Welcome to the Quiz Game")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    print("Goodbye")
    quit()

print("Okay! Let's play:)")
score = 0

name = input("Please enter your name: ")
print("Hello, " + name)

answer = input("How many countries start with the letter 'A'? ")
if answer.lower() == "sixteen":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What American president appears on a one-dollar bill? ")
if answer.lower() == "george washington":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many colors are there in a rainbow? ")
if answer.lower() == "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What is the nickname of the US state of California? ")
if answer.lower() == "golden state":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What restaurant's mascot is a clown? ")
if answer.lower() == "mcdonald's":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")
