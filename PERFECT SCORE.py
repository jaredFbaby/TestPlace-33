#purpose of the program
print("Grade Calculator")
print("-----------------")

#declare variables
assignmentCount = 1
finalScore = float(0)
score = float(0)
#intro logic
numAssignments = int(input("How many assignments are in this class? "))
#incoming information
while assignmentCount <= numAssignments:
    enteredScore = input( "What is the score for assignment no." + str(assignmentCount) + "? ")
    score += float(enteredScore)
    assignmentCount += 1
#final math
finalScore= score / numAssignments
print("Your final score is", finalScore,"%" )
