def BubbleSort(array):
    # The outer loop goes through the elements n-1 times, if n is the number of elements in the list

    for num in range(len(array)-1,0,-1):
        # count down to 0 as each time another element at the end of the list is sorted.
        # at each pass the last i elements are already in place so the inner loop is shorted by 1 each time
        for i in range(num): 
            # comparing each element i with the element right beside it (i+1)  
            if array[i] > array[i+1] : 
                # If the elements are out of order swap them so the largest element is right of the smaller one
                array[i], array[i+1] = array[i+1], array[i]
    