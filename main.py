

from typing import List, Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode 



class Solution:

    #--- SLIDING WINDOW ---
    
    # design an algorithm to find the maximum profit in a given stock portfolio
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = buy, right = sell
        max_profit = 0

        #as long as the right index is less than the length of the prices list
        while r < len(prices):
            #profitble if the price is higher than the previous price
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                #check if the profit is greater than the current max profit
                max_profit = max(profit, max_profit)
            else:
                #if the price is lower than the previous price, reset the left index
                l = r
            r += 1
        return max_profit

    # given a string, find the lenght of the longest substring without repeating characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 #left index
        res = 0 #current max length

        for r in range(len(s)):
            #if the current char is in the charSet, remove it
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 #move the left index
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

    # given 2 strings s and t, return the minimum window substring of s in which all the characters in t appear, if there is no such substring return the empty string
    def minWindow(self, s: str, t: str) -> str:
        #if the string t is empty, return the empty string
        if t == "": return ""
        
        #init the count and window hashmaps
        countT, window = {}, {} 
        res, resLen =  [-1, -1], float("infinity")
        l = 0 #left index
        for c in t:
            countT[c] = countT.get(c, 0) + 1 #get the count of the current chars in t - if not set will return 0

        have, need = 0, len(countT) #have = the number of chars in t, need = the number of chars in s
        #as long as the right index is less than the length of the string s
        for r in range(len(s)):
            ch = s[r] #current char
            window[ch] = window.get(ch, 0) + 1 #get the count of the current char in the window - if not set will return 0

            if ch in countT and window[ch] == countT[ch]:
                #we satisfied a match in the need, so add the current char to the result
                have += 1

            while have == need:
                #update the result
                #if the size of the result is less than the current result,update it (which starts as infinity)
                if (r -l + 1) < resLen:
                    #update the result
                    res = [l, r] #window
                    resLen = (r - l + 1) # result/window length

                #pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 #move the left index

        l, r = res 
        #if the result is infinity, return the empty string
        return s[l:r+1] if resLen != float("infinity") else ""



    #--- BINARY SEARCH ---
    # given an array of integers nums and an integer m, split the array into m non-empty subarrays, the task is to find the largest sum of a subarray and return its length
    def splitArray(self , nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums) #left: max value in array, right: sum of values
        res = r
        
        def canSplit(largest):
            #subarrays count
            subarray = 0
            #current sum of the subarrays
            curSum = 0
            #loop through the nums
            for n in nums:
                #add the current num to the current sum
                curSum += n
                if curSum > largest:
                    #add to the subarray count
                    subarray += 1
                    #reset the current sum
                    curSum = n
            #return if the subarray count is less than or equal to the m
            return subarray + 1 <= m    

       
        while l <= r:
            #get the middle index
            mid = l + ((r - l) // 2)
            #split the nums into m subarraysand check if the values are less than the middle index
            if canSplit(mid):
                #set the res to the middle index
                res = mid
                #if we can split, update the right index
                r = mid - 1
              
            else:
                #if we can't split, update the left index
                l = mid + 1
        return res        

    #given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    def binarySearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 #left - start of array, right - end of array

        while l <= r:
            #get the middle index
            mid = l + ((r - l) // 2)
            #if the middle index is greater than the target, update the right index
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                #if the middle index is less than the target, update the left index
                l = mid + 1
            else:
                #if the middle index is equal to the target, return the middle index
                return mid
        return -1

    #given a positive integer num, write a function which returns True if num is a perfect square else False
    def validPerfectSquare(self, num: int) -> bool:
        l,r = 1, num
        while l <= r:
            mid = l + ((r - l) // 2)

            if mid * mid > num:
               r = mid - 1
            elif mid * mid  < num:
               l = mid + 1
            else: 
               return True
        return False


    #--- BALANCED BINARY TREE ---
    # given a binary tree, check whether it is height-balanced
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            #check if the root is None, then return True and 0 which is the height
            if not root: return [True, 0]

            #recursive call to the left and right subtrees to check if they are balanced
            left, right = dfs(root.left), dfs(root.right)
            #if the left and right subtrees are balanced and the height of the main tree is balanced
            balance = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            return [balance, max(left[1], right[1]) + 1]

        return dfs(root)[0]

    #invert a binary tree
    def invertTree(self, root: TreeNode) -> TreeNode:
        #if the tree is empty, return None
        if not root: return None

        #invert the left and right subtrees
        tmp = root.left
        root.left = root.right
        root.right = tmp
        #invert the left and right subtrees of the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


#input: prices = [7, 1, 5, 3, 6, 4]
#output: 5
#buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5
#not 7-1 = 6 because the profit is not greater than the current max profit
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

#input: "abcabcbb"
#output: 3
#the answer is "abc", with the length of 3
print(Solution().lengthOfLongestSubstring("abcabcbb"))

#input: s = "ADOBECODEBANC", t = "ABC"
#output: "BANC"
#the answer is "BANC"
print(Solution().minWindow("ADOBECODEBANC", "ABC"))

#input: nums = [7, 2, 5, 10, 8 ], m = 2
#output: 18
#the best way to split the array is [7, 2, 5, 10, 8] into [7, 2, 5] and [10, 8] where the sum of the subarrays is 18 and the length of the subarrays is 2
print(Solution().splitArray([7, 2, 5, 10, 8], 2))

#input: nums = [1,2,3,4,5] m=2
#output: 9
print(Solution().splitArray([1, 2, 3, 4, 5], 2))

#input: nums = [-1, 0, 3, 5, 9, 12], target = 9
#output: 4
#the target exists in the array, so return the index 4
print(Solution().binarySearch([-1, 0, 3, 5, 9, 12], 9))

#input: nums = [-1, 0, 3, 5, 9, 12], target = 2
#output: -1
#the target does not exist in the array, so return -1
print(Solution().binarySearch([-1, 0, 3, 5, 9, 12], 2))

#input: num = 16
#output: True
#the number is a perfect square, so return True
print(Solution().validPerfectSquare(16))

#input: num = 14
#output: False
#the number is not a perfect square, so return False
print(Solution().validPerfectSquare(14))


#Input: root = [3, 9, 20, null, null, 15, 7]
#Output: True
#The tree is balanced
root = creatBTree([3, 9, 20, None, None, 15, 7], 0)
print(Solution().isBalanced(root))


#Input: root = [1, 2, 2, 3, 3, 3, null, null, 4, 4, 4, 5, 5, 5]
#Output: False
#The tree is not balanced
root = creatBTree([1, 2, 2, 3, 3, 3, None, None, 4, 4, 4, 5, 5, 5], 0)
print(Solution().isBalanced(root))