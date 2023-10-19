sale = []

#for i in sale: 
    
total = 0 
count = 0
while count < 6:
    newSale = int(input("Please enter a sale:\n"))
    sale.append(newSale)
    print(sale)
    count += 1 
    total = total + newSale
print(total)
