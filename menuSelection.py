#centimeters = inches * 2.54
#meters = feet * 0.3048
#kilometers = miles * 1.609

#convert inches to centimeters
#convert feet to meters 
#convert miles to kilometers

#enter your selection 
print("--Main menu--")
print("1. Convert inches to centimeters.")
print("2. Convert feet to meters.")
print("3. Convert miles to kilometers.")
print()
menuSelection = int(input("Enter you selection:"))
while menuSelection <1 or menuSelection>3:
    print("That is invalid")
    menuSelection = int(input("Enter 1, 2, or 3:"))
#Now perform the selected operation
if menuSelection ==1:
    #Convert inches to centimeters
    inches = float(input("Enter the number of inches"))
    centimeters = inches *2.54
    print("That is equal to",centimeters, "centimeters.")
elif menuSelection == 2:
    #Convert feet to meters 
    feet = float(input("Enter the number of feet:"))
    meters = feet * 0.3048
    print("That is equal to", meters, "meters.")
elif menuSelection ==3:
    #Convert miles to kilometers 
    miles = float(input("Enter the number of miles:"))
    kilometers = miles * 1.609
    print("That is equal to", kilometers,"Kilometers.")
 
