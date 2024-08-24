# Welcome to Day 1 of the DSA Coding Challenge:

# Today's Goals (Arrays) :
# -Learn Big O Analysis to find Time and Space complexity
# -Array Data Structure


## Complexity Analysis, Big O 

# What is the need of complexity analysis?
    #* The need of complexity analysis is to measure the performance or time complexity of an algorithm. It helps.

# What is time complexity?
    #* Time complexity is the amount of time an algorithm takes in terms of the size of the input, typically represented as 'n'.

# Asymptotic Analysis?
    #* Asymptotic analysis is a method of analyzing the time and space complexity of an algorithm. It helps us understand how an algorithm's running time or memory usage grows as the input size increases.
    #* Eg. f(N) = N + 3 
    #* if input N -> becomes very large the constant 3 is insignificant or neglegible.
    #* So we can say the time complexity of the function is O(N), which is linear in this case.

# What is Big O?
    #* Big O notation is way to represent or describe the performance of an algorithm, which is the amount of time or space it requires as the input size increases.
# Common Complexities
    #** O(1) - Constant time complexity
    #** O(log n) - logarithmic time complexity
    #** O(n) - Linear time complexity
    #** O(n log n) - Linearithmic time complexity: The algorithm takes proportional time to the product of the size of input and its logarithm.
    #** O(n^2) - Quadratic time complexity: It grows as the squared the size of input.
    #** O(2^n) - Exponential time complexity, where the execution time grows exponentialy as the size of input increases. 
    #**  O(n!) - Factorial time complexity: This is the worst time complexity, which grows factorially with the input size. It takes time proportianal to the factorial of the size of input (N).

# Space complexities?
    #* Space complexity refers to the amount of memory an algorithm uses or requires for execution. 
    # * For Example: Referring to the merge sort algorithm - O(n log n)
        #** arr = [2,1, 9, 5, 7, 3,4]
        #** mid = len(arr) // 2 = 3;
        #** left = arr[:mid] = [2, 1, 9]
        #** right = arr[mid:] = [5, 7, 3, 4]
        #** Sorting Algorithms: Merge Sort
        #** while len(left) > 0 and len(right) > 0:
        #** if left[0] <= right[0]
        #** pop [0] of left and append -> result = []
        #** else pop [0] of right and append -> result = []
        #** extend left -> result[]
        #** extend right -> result[]
        #** return result

# Techniques of specifying Time Complexity?
    #* Drop Constant: O(25n^2)
        #** suppose If n=1000 the constant 25 is insignificant which can be dropped here
    #* Drop Lower Order or insignificant Terms: O(n^2 + n) or O(n^2 + 100n)
        #** If n is large, the lower order term of n is insignificant which can be dropped here and it will be O(n^2)
    #* Different input parameters O(n + m)
        #** O(n + m) where n and m are input parameters and m cannot be dropped as in some cases it could greated than m

# Logarithm in time and space complexit?
    #* Logarithmic space/time complexity is a measure of how the runtime of an algorithm scales as the input grows. It is the time complexity that grows very slow as the input size grows.

    #* In coding -> log 2base n -> log n
        #** n=16 -> log 2base 16 -> 16 = 4 -> 2^4 = 16
        #** log 8 -> 2^? -> 2^3 -> 3
            #*** For Example:
            #*** n = 1024 -> log n -> log 1024 -> log 2^10 -> 10
            #*** n = 1048576 -> log n -> log 1048576 -> log 2^20 -> 20
    #* Algorith that cuts I/p half at every step
        #** n=8; 8-->4-->2-->1; step=3
    #* If you double the input only one extra step will get added
        #** n=16; 16-->8-->4-->2-->1; step=4 

# Array?
    #* Array is a built-in data structure that stores a collection of elements in contiguous memory location. 
    #* Each elements is stored at an index (0, 1, 2, ...).
    #* Any element can be read or write/inserted using the index of that element.
    #* It has a fixed length which can be defined during the declaration of an array.

    #* Big O of common array operations:
        #** Accessing an element: S(space compexity),T(Time complexity) = O(1)
        #** Insertion:
            #*** beginning: S, T = O(1), O(n)
            #*** end: S, T = O(1); if the array is full T = O(n)
            #*** somewherein b/w: S, T = O(1), O(n)
        #** Deletion:
            #*** beginning: S, T = O(1), O(n)
            #*** end: S, T = O(1)
            #*** somewherein b/w: S, T = O(1), O(n)
        #** Set: S, T = O(1)
        #** Copy: S, T = O(n)
        #** Traverse/Search: S, T = O(1), O(n)


# Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.


# Example: Input: [-5, -3, 0, 3, 4]
# Example: Output: [0, 9, 9, 25, 16]

# Method 1
def squared_array(inputArr):
    arrLength = len(inputArr)
    outputArr = [0]*arrLength
    for i in range(arrLength):
        outputArr[i] = inputArr[i] ** 2

    outputArr.sort()
    return outputArr

arr1 = [-5, -3, 0, 3, 4]
print(squared_array(arr1))

# Big O Notation for the above solution: S, T = O(n), O(n log n)

# Method 2
def squared_sorted_array(inputArr):
    n = len(inputArr)
    i, j = 0, n - 1
    outputArr = [0]*n
    for k in reversed(range(n)):
        print(k)
        if inputArr[i]**2 > inputArr[j]**2:
            outputArr[k] = inputArr[i]**2
            i += 1
        else:
            outputArr[k] = inputArr[j]**2
            j -= 1
            
    outputArr.sort()
    return outputArr

arr1 = [-5, -3, 0, 3, 4]
print(squared_sorted_array(arr1))


# Question 2: Monotonic Array - An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.

# Example: Input: [1, 2, 2, 3]

def isMonotone(inputArr):
    increasing = decreasing = True
    for i in range(len(inputArr) - 1):
        if inputArr[i] < inputArr[i + 1]:
            increasing = False
        elif inputArr[i] > inputArr[i + 1]:
            decreasing = False
    return increasing or decreasing

arr1 = [1, 2, 3, 4]
print(isMonotone(arr1))

# Big O Notation for the above solution: S, T = O(1), O(n)





