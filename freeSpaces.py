def nextMove(passengers):
    answer = input("Want to check a plane? ")
    answer.lower()
    
    yesAnswer = ["y"]
    noAnswer = ["n"]
     
    if answer in yesAnswer:
        print("This are the passengers: ")
        passengersIndex = int(len(passengers))
        passengersIndex -= 1
        
        indexCount = -1
        
        for passengersIndex in range(len(passengers)):
            print(passengers[passengersIndex])
            passengersIndex -= 1
    elif answer in noAnswer:
        print("Shutting down...")        
    else:
        print("Wrong input, please enter y or n.")
        nextMove(passengers)
       
       
def addPerson(free, places):
    if free > 0:
        passengers = []

        for i in range(free):
            nameInput = input("Enter the passenger's name: ")
            passengers.append(nameInput)
            
            free -= 1
            
            if free == 0:
                nextMove(passengers)
                return passengers


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
    
except TypeError():
    print("There is no input, please enter a number.")