#Python bubble sort 
def bubbleSet(arr):
    n = len(arr)
    #optimize code, so if the array is already sorted, it doesn't meed to go through the entire process
    #Transverse through all array elements
    for i in range(n-1):
        #range(n) also work but outer loop will 
        #repeat one time more than needed 
        #Last i elements are already in place 
        for j in range (0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True 
                arr [j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            #if we haven't needed to make a single swap, we 
            #can just exit the main loop 
            return 
#Driver code test above 

arr = [7,2,3,8,9,1]
bubbleSet(arr)
print("Sorted array is:")
    
for i in range(len(arr)):
            print("% d"%arr[i], end=" ")
        
