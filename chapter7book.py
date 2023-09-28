#the markup is used as a global constant
#the markup is percentage 
MARK_UP = 2.5
#the main function
def main():
#Variable to control the loop 
    another = "y" 
#Process one or more items 
    while another == "y" or another == "Y":
        #Display ann item's retail price 
        show_retail()
        
        #Do this again?
        another == input("Do you have another item?") + ("Enter y for yes): ")
        
    #The show_retail function gets an item's wholesale
    #cost and displays the item's retail price
def show_retail(): 
        #Get the items wholesale cost
    wholesale = float(input("Enter the item's wholesale cost:"))
        #validate the wholesale cost
    while wholesale <0: 
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the wholesale cost:"))
            #calculate the retail price
    retail = wholesale * MARK_UP
            
            #Dispplay the retail price 
    print("The retail price is $",format(retail, ".2f"))
            
     #call the function
main()       
        
