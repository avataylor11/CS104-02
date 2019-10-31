#Sum/Average Program
#Your first and last name: Ava
#Your student ID: Taylor

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberList = []
sumInt = 0
avgInt = 0.0

for x in range (0,20):
    number = int(input ("Enter a number: "))
    numberList.append(number)
    sumInt+=numberList[x]

print(numberList)

avgInt=(sumInt/(len(numberList)))

print("The sum of the numbers that you entered is ", sumInt)
print("The average of the numbers that you entered is ", avgInt)



#print("The sum of the numbers that you entered is ", sum(numberList))

#print("The avergae of the numbers that you entered is ", (sum(numberList)/len(numberList)))
