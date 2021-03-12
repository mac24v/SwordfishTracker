#Marshall Callaway

#This program will help store and document the fish we have caught during commercial fishing trips to help  keep records of the amount of fish we caught, the price we recieved for the fish and other related specifications related to the fish.
#I commercial fish in Fort Lauderdale for some of the year and this would help keep documetation of the fish we have caught and keep track of profits
#We have had trouble in the past with keeping up with this information

print("Hello,", end=' ')
print("welcome  to the Fish Recorder")

dayCaught =  input("Enter when the fish was caught mm/dd/yyyy:")

#Might add a section for coordinates(lat/long) but I am not sure yet
fishLocation = input("Enter the location that the fish was caught:")

tripLength = input("Enter the total amount of hours at sea:") 

boatName = input("Enter the name of the boat:")

boatType = input("Enter the type of boat:")

#We would use 24hr time for this instead of am or pm
timeCaught = input("Enter the time the fish was caught:")

fishType = input("Enter the type of fish caught:")

#For length and girth we use inches when we fish
fishLength = input("Enter the length of the fish:")

fishGirth = input("Enter the girth of the fish caught:")

fishWholeweight = float(input("Enter the weight of the whole fish:"))

#Core weight is without head, fins, guts or tail
fishCoreweight = float(input("Enter the weight of the fish after it is cored:"))

poundPrice = float(input("Enter the price per pound recieved for fish:"))

gearGone = input("Enter the gear lost during the trip:")

gearLost = float(input("Enter the amount of money lost in gear:"))

distanceTraveled = float(input("Enter  the amount of miles traveled:"))

fuelUsed = int(input("Enter the the gallons of fuel burned:"))

fuelPrice = float(input("Enter the price per gallon of  fuel:"))

#Calculations used to help find total money spent and made
fuelCost = fuelUsed  * fuelPrice
fishProfit = fishCoreweight * poundPrice
tripMPG = distanceTraveled  /  fuelUsed
totalProfit  = fishProfit - fuelCost  - gearLost

print("Date:", dayCaught)

print("Location:", fishLocation)

print("Total time spent fishing:", tripLength, "hours")

print("Boat fished on:", boatName +','+' '+ boatType)

print("Time of catch:", timeCaught)

print("Type of fish:", fishType)

print("Fish length in inches:", fishLength)
print("Fish girth in inches:", fishGirth)

print("Whole fish weight:", fishWholeweight)
print("Cored weight:",  fishCoreweight)

print("Total miles traveled:", distanceTraveled)
print("Average trip MPG:", format(tripMPG, "0.2f"))

print("Gear needed for next trip:", gearGone)

print("Gear lost: $", format(gearLost, "0.2f"), sep='')
print("Fish total price: $", format(fishProfit, "0.2f"), sep='')
print("Fuel cost: $", format(fuelCost, "0.2f"), sep='')
print("Profit made: $", totalProfit, sep='')

#Used the POGILs to help with formating and all the other things I used were from everything we have had problems with before or needed to document
