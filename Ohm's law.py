potentialDifferenceSymbol = "vb".upper().strip()
currentIntensitySymbol = "i".capitalize().strip()
totalResistorsSymbol = "r".capitalize().strip()
internalResistorSymbol = totalResistorsSymbol.lower()
# Symbols of Ohm's law
potentialDifferenceSymbolByOhmLaw = f"{potentialDifferenceSymbol} = {currentIntensitySymbol} * ( {totalResistorsSymbol} + {internalResistorSymbol})".strip()
currentIntensitySymbolByOhmLaw = f"{currentIntensitySymbol} = {potentialDifferenceSymbol} / ( {totalResistorsSymbol} + {internalResistorSymbol})".strip()
totalResistorsSymbolByOhmLaw = f"{totalResistorsSymbol} = ( {potentialDifferenceSymbol} / {currentIntensitySymbol} ) - {internalResistorSymbol}".strip()

print(potentialDifferenceSymbolByOhmLaw)
print(currentIntensitySymbolByOhmLaw)
print(totalResistorsSymbolByOhmLaw)

# This is law in real

internalResistor = input("What\'s value of internal resistor?").strip()
potentialDifference = input("What\'s value of potential difference?").strip()
currentIntensity = input("What\'s value of current intensity?").strip()
totalResistors = input("What\'s value of total resistors?").strip()

# Potential difference

if potentialDifference == "V" or potentialDifference == "v":
    if int(internalResistor) == int(0):
        print("Your potential difference between the battery terminals is")
        print(int(currentIntensity) * int(totalResistors))
        print("Volt")
    elif int(internalResistor) != int(0):
        print(int(currentIntensity) * (int(totalResistors) + int(internalResistor)))
        print("Your potential difference between the battery terminals is")
        print("Volt")

# Current intensity

elif currentIntensity == "I" or currentIntensity == "i":
    if int(internalResistor) == int(0):
        print("Your current intensity is")
        print(int(potentialDifference) / float(totalResistors))
        print("Amber")
    elif int(internalResistor) != int(0):
        print("Your current intensity is")
        print(int(potentialDifference) / (float(totalResistors) + float(internalResistor)))
        print("Amber")

# Total resistors

elif totalResistors == "R":
    if int(internalResistor) == int(0):
        print("Your total resistors is")
        print(int(potentialDifference) / int(currentIntensity))
        print("ohm")
    elif int(internalResistor) != int(0):
        print("Your total resistors is")
        print((int(potentialDifference) / int(currentIntensity)) - int(internalResistor))
        print("ohm")

    # Internal resistor
elif internalResistor == "r":
    print("Your internal resistor is")
    print((int(potentialDifference) / int(currentIntensity)) - int(totalResistors))
    print("ohm")

# Finished
