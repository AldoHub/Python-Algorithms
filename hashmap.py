#--- HASHMAP ---


#--- two sum ---
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums: list[int], target: int) -> list[int]:
    #create and empty hashmap
    num_to_index = {} # will store the index of the number in the array

    #we use enumerate to iterate over the array - will give us the index and the value
    for i, num in enumerate(nums):
        #print(f"num: {num}")
        #print(f"i: {i}")
        #calculate the complement - the number that, when added to the current number, will give the target
        complement = target - num # for example, if the target is 9 and the current number is 2, the complement is 7
        print(f"complement: {complement}")

        #check if the complement is in the hashmap
        if complement in num_to_index:
            #the current and the compliment add up to the target
            return [num_to_index[complement], i]

        #if the complement is not in the hashmap, we add it
        num_to_index[num] = i

    return []

print(two_sum([2,7,11,15], 9))