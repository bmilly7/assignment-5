# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input:
numbers = [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    
    count = {}
    for i in numbers:
        count[i] = count.get(i,0) + 1

        frequent = max(count, key=count.get)

    return frequent

result = most_frequent(numbers)
print("problem 1: ")
print(result)
print("--------------------------")
"""
Time and Space Analysis for problem 1:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: 
nums = [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    new_list = []

    for i in nums:
        if i not in new_list:
            new_list.append(i)
    return new_list

result = remove_duplicates(nums)
print(f"problem 2 result: {result}")
print("-----------------------------")

"""
Time and Space Analysis for problem 2:
- Best-case:o(n^2)
- Worst-case:o(n^2)
- Average-case:O(n^2)
- Space complexity:
- Why this approach? This was the simpliest way in my head to get the solution for the problem. It is okay for small data but will not be as efficient as the data grows
- Could it be optimized? 
Yes, it could be optimized by using a set to check for the lookups o(1) instead of o(n)
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: 
nums = [1, 2, 3, 4]
target=5
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = {}

    for i in nums:
        compliment = target - i
        if compliment in nums: 
                pairs[i] = compliment
                nums.remove(i)

    return pairs

result = find_pairs(nums, target)
print(f"problem 3 result: {result}")
print("-----------------------------")

"""
Time and Space Analysis for problem 3:
- Best-case:o(n^2)
- Worst-case:o(n^2)
- Average-case:o(n^2)
- Space complexity:o(n)
- Why this approach? This was the first method that came to my mind to solve this problem
- Could it be optimized?
Yes, after research, this also could be optimized by using a set as well to keep up with the seen values and their compliment
You can also keep the pairs unique by always adding the pairs with lowest value first. this way the set automatically removes duplicated pairs. (1,4) (4,1)"""
#optimized solution at bottom of file

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.
n = 6

def add_n_items(n):
    
    capacity = 4          # initial capacity
    size = 0              # current number of items
    items = []            # our list

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} → {new_capacity}")
            capacity = new_capacity
            # Simulate copying existing items
            print(f"Copying {size} items to new list")
        
        items.append(i)
        size += 1

    print(f"Final list: {items}")
    print(f"Final capacity: {capacity}")

print(f"problem 4 result: {add_n_items(6)}")
"""
Time and Space Analysis for problem 4:
- When do resizes happen? resizing happens when the array runs of out space. It creates a new array with more memory space and copies the existing elements int the new array
- What is the worst-case for a single append? for a single append is o(n) if trigger resize
- What is the amortized time per append overall? the amortized time per append overall is also o(1) because it is accepted that the operation is generally fast
- Space complexity: o(n) based on n number of items
- Why does doubling reduce the cost overall?  Doubling ensures fewer resizes are needed as list grows → total cost spread out → amortized O(1)
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: 
nums = [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
   
    new_list = []
    total = 0  # running sum
    for i in nums:
        total += i          # add current number to running total
        new_list.append(total)  # append running total to new list
    return new_list

result = running_total(nums)
print(f"problem 5 result: {result}")
print("-----------------------------")

"""
Time and Space Analysis for problem 5:
- Best-case:O(n)
- Worst-case:O()
- Average-case:O(n)
- Space complexity:O(n)
- Why this approach? keeps running total in variable instead of recomputing sums repeatedly
- Could it be optimized? this is optimal
"""





#optimized for problem 3: 
def find_pairs(nums, target):
    seen = ()
    pairs = ()

    for i in nums:
        compliment = target - i
        if compliment in seen:
            pairs.add((min(i, compliment)), (max(i,compliment)))
        seen.add(i)

    return list(pairs)



"""
 This utilizes a set for quicker lookups O(1) instead of searching through an array. 
 Each number is processed once (O(n) loop).

in seen check → O(1) average time because sets use hashing.

You only store what’s needed (the numbers you’ve seen so far).

pairs is also a set to avoid duplicates, e.g. (2, 3) and (3, 2) are treated as the same because you always use (min, max) order.
"""