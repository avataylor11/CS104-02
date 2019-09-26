import random
theComputerNumber = (random.randint(1,1000000))

#cheat = str(theComputerNumber)
#print(cheat)

gameOver = False

numberOfGuesses = 0
guess = 0

lowGuessRange = 1
highGuessRange = 1000000

print ("Hello! Welcome to the guessing game! You have 20 tries to guess my random number between 1 and 1000000. Good Luck!")


#This is a game loop
while gameOver != True and numberOfGuesses <= 20 and guess != theComputerNumber:
    
    guess = int (input ("Enter a guess: "))

    if guess < lowGuessRange or guess > highGuessRange:
        print("Your guess is out of range")
        
    elif guess < theComputerNumber:
        print ("Your guess is too low :( ")
        lowGuessRange = guess
        #guess = str(guess)
        lowGuess = str(lowGuessRange)
        highGuess = str(highGuessRange)
        print ("Enter a guess from " + lowGuess + " to " + highGuess + " " )

    elif guess > theComputerNumber:
        print ("Your guess is too high :( ")
        highGuessRange = guess
        #guess=str(guess)
        lowGuess = str(lowGuessRange)
        highGuess = str(highGuessRange)
        print ("Enter a guess from " + lowGuess + " to " + highGuess + " " )
           
    else:
        gameover = True
        print ("you guessed it! :) ")

    numberOfGuesses += 1

if guess == theComputerNumber:
    numberOfGuesses = str(numberOfGuesses)
    print("Congrats, you guessed the number in " + numberOfGuesses + " guesses")

if guess != theComputerNumber:
    theComputerNumber = str(theComputerNumber)
    print("You ran out of guesses, the number you were looking for was " + theComputerNumber + "!")



#guess = int (input ("Enter a guess from " + lowGuess + " to " + highGuess + ": "))
#guess = int (input ("Enter a guess from " + lowGuess + " to " + highGuess + ": " ))





