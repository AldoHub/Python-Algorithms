#--- SLIDING WINDOW ---
#is an extension of the two pointers pattern
#use sliding window pattern when you face problems like: WORD SEARCH, WORD BREAK, CONTIGUOUS SUBARRAY SUM,

#--- FIXED SIZED SLIDING WINDOW
#given an array of nums consisted of only non-negative integers, find the largest sum among all sub-arrays of length k in nums

#for example, given the nums = [1, 2, 3, 7, 4, 1 ] and k = 3, then the output would be 14
#as the largest lenght 3 subarray sum is given by [3, 7, 4], which sums to 14

from collections import defaultdict
from typing import List


def subarray_sum_fixed(nums: List[int], k: int) -> int:
    #build the window
    window_sum = 0
    #sum all the elements in the window
    for i in range(k):
        window_sum += nums[i]

    #store the current sum so far
    largest_sum = window_sum

    for right in range(k, len(nums)):
        #remove the first element from the window
        left = right - k 
        #remove from the total sum, the element that was removed
        window_sum -= nums[left]
        #add the new element to the window and sum it
        window_sum += nums[right]
        #if the sum is larger than the current largest sum, update the largest sum
        largest_sum = max(largest_sum, window_sum)

    return largest_sum


#--- DYNAMIC SIZED SLIDING WINDOW
# find the lenght of the longest substring of a given string without repeating characters

def longest_substring_without_repeating_characters(s: str) -> int:
    longest = 0
    left = 0
    #track the number of times each character appears in the current window
    counter: dict[str, int] = defaultdict(int)

    #loop through the string
    for right in range(len(s)):
        #add to the window
        counter[s[right]] += 1
        #check if the char is repeating
        #shrink the window from the left
        while counter[s[right]] > 1:
            #remove elements from the left
            counter[s[left]] -= 1
            #move the left pointer
            left += 1

        #if the window is the longest, update the longest
        longest = max(longest, right - left + 1)

    return longest