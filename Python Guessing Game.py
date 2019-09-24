import random
theComputerNumber = (random.randint(1,1000000))

gameOver = False

numberOfGuesses = 0

lowGuessRange = 0
highGuessRange = 1000000

guess = int (input ("Enter a guess: "))
#This is a game loop
while gameOver != True:
    numberOfGuesses + 1
   
    if guess < theComputerNumber:
        print ("guess is too low")
        lowGuessRange = guess
        guess = str(guess)
        lowGuessRange = str(lowGuessRange)
        highGuessRange = str(highGuessRange)
        guess = int (input ("Enter a guess from " + lowGuessRange + " to " + highGuessRange + ": "))

    elif guess > theComputerNumber:
        print ("guess is too high")
        highGuessRange = guess
        guess=str(guess)
        lowGuessRange = str(lowGuessRange)
        highGuessRange = str(highGuessRange)
        guess = int (input ("Enter a guess from " + lowGuessRange + " to " + highGuessRange + ": " ))
       
    else:
        gameover = True
        print ("you guessed it!")







