def flatten_and_sort(array):
    arr = []
    for item in array: #Loops through every item of array
        for i in item:
            arr.append(i) 
            
            #Appends each item in that specific array to the new array called arr, once it finishes the first array, it will move onto the next set of integers array in the provided array, ex [[1,2,3], [4,6,5]] being the provided array. [1,2,3] being the first set of integer arrays and [4,6,5] coming after it.
    
    return sorted(arr) #Sort will sort it in ascending order


#print(flatten_and_sort([[6,2,8], [1,3,4]]))  <- This was a test run

#How does this solution ensure data immutability?
# It ensures data immutability as the data is within the function itself so it cannot be changed due to it being a pure function. 

#Is this solution a pure function? Why or why not?
# This solution is pure due to no data being changed outside of the function, the data that is changed is the arr variable which is within the function.

#Is this solution a higher order function? Why or why not?
# It is not a high order function as it does not take a function as an argument or return a function as an output

# Would it have been easier to solve this problem using a different programming style?
# It would be easier to solve it using functional programming instead of anything else.

#Why in particular is functional programming a helpful paradigm when solving this problem?
# When solving this problem, it is easier to use functional programming as you are not manipulating any attributes. All you are doing is inserting an argument and wanting a specific outcome in return, in this example it is a flattened and sorted array in ascending order.