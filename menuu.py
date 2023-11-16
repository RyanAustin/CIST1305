thePost = []
def menu():
    thePost = "October 24th Scorpio"

    print("Welcome to the post of the day!")
    print("Please slect the option of your choice")
    print("1) Add new entry for today")
    print("2) View Entries.")
    print("3) You can exit.")

    choice = input("Your selection")

    if choice =="1":
        print("Adding your new caption for today.") 
        getPost()
    elif choice == "2":
        print("Viewing entries you have.")
        print(thePost)
    
    elif choice == "3":
        print("Exiting.")
    else:
        print("That is a invalid selection.")

def getPost():
   print("What would you like to put in your post")

   post = str(input("Please input post"))
   
   print(post)
   return post
def thePost():
    print(thePost)

menu()
