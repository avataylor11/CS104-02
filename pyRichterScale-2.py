#Python Richter Scale Calculation
#Your first and last name:
#Your ID:

#Requirements Version 1:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

#Additional Requirements Version 2:
# ask the user to 'Enter the Richter scale value or -99 to end: '
#   continue the program until the user enters a richter value of -99
#   if richter = -99, end the program
#   hint1: use a 'while' loop with a 'boolean' like in the guessing game
#   hint2: 'break' may come in handy

# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
#   and make them enter another value
#   hint: 'continue' may come in handy


# Test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

gameOver = False
while gameOver != True:
    richter=float(input("Enter richter scale value"))
    if richter >= 8.0:
        print("Most structures fall")
    elif richter >= 7.0:
        print("Many buildings destroyed")
    elif richter >= 6.0:
        print("Many buildings considerably damaged, some collapse)
    elif richter >= 4.5:
        print("Damage to poorly constructed vehicles")
    elif richer <= 4.5:
        print("No destruction of buildings")
    else:
        print(" ")
    again=str(input("Enter yes or no if you would like to test another value"))
    if again == yes:
        gameOver = False
    elif:
        gameOver = True
        
