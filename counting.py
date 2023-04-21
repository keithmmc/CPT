def CountingSort(array):
    n= len(array)
    # creating a counter array initialised with zeros, length based on maximum value in the input range (plus 1)
    # counter to record each time each unique value occurs
    counter= [0 for i in range(max(array)+1)]
    # an array to store the sorted values
    sorted = []   
    # loop over each element, use the element of the array input as the index for the counter array
    for i in array:
        # each time an element appears in the array, increment the counter by 1
       counter[i] += 1
    # Using the count of the number of times each element occurs to place elements in the sorted array

    for i in range(0,len(counter)):
        # while the counter shows that there is a matching element
        while counter[i] > 0:
            # append the element to the sorted array
            sorted.append(i)
           # decrease the counter by 1 each time
            counter[i] -= 1
    return sorted

                 
    
    