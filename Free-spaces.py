def addPerson(free, places):
    if free > 0:
        passengers = []
        for i in range(free):
            nameInput = input("Enter the passenger's name: ")
            passengers.append(nameInput)

print("Welcome to the placing system!")

try:
    totalPlaces = int(input("How many places are there? "))
    freePlaces = int(input("How many free places are there? "))
    
    if freePlaces > totalPlaces:
        print("Error: You can't have more free places than there are places!")
    elif freePlaces < totalPlaces:
        addPerson(freePlaces, totalPlaces)
    elif freePlaces == totalPlaces: 
       addPerson(freePlaces, totalPlaces)

except ValueError():
    print("Wrong input, please enter a number.")
    main()
