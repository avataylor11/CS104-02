names = []
numEntries = 0
end = False
while end != True and numEntries < 10:
    name = (input ("Enter a name: "))
    names.append(name)
    numEntries += 1

#print(names)

while end !=True:
    search = (input ("Enter a name to search for or 'end' to end the program: "))
    if search in names:
        print (search, "was found!")
    elif search == "end":
        end = True
    else:
        print (search, "was not found :( ")

print ("You have ended the program!")
 
