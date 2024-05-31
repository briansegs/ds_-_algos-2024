'''
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
'''

# My solution

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    max_curr = arr[0]
    max_global = arr[0]
    
    for num in arr[1:]:
        max_curr = max(max_curr + num, num)
        max_global = max(max_curr, max_global)
        
    return max_global

# Tests

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
