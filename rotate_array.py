


def rotate(arr,k):
    for i in range(0,k):
       
        last = arr[-1]
        arr.remove(last)
        arr.insert(0,last)
    return arr

arr = [1,2,3,4,5,6,7]
k = 3
print(rotate(arr,k))

# Taking time and space complexity
# Method 1: Brute Force
# Time Complexity: O(n*k)
# Space Complexity: O(1)

# Method 2: Using extra array
# Time Complexity: O(n)
# Space Complexity: O(n)

# Method 3: Using Juggling Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 4: Using Reversal Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

