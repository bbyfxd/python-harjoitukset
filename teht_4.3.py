userInput = input("Sano luku: ")
maxValue = minValue = int(userInput)

while True:
    userInput = input("Sano luku: ")
    if userInput == "":
        break
    userInputInt = int(userInput)
    if userInputInt < minValue:
        minValue = userInputInt
    if userInputInt > maxValue:
        maxValue = userInputInt
print(f"Pienin arvo: {minValue}, Suurin arvo: {maxValue}")