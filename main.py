

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

class ListNode:
    """A standard node definition for a singly-linked list."""
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val: int = val
        self.next: Optional['ListNode'] = next_node

    def __repr__(self) -> str:
        """Visual helper to print the list sequence."""
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes)


def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a standard Python list into a linked list structure."""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list back into a standard Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result



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

    #given a binary tree, count the number of good nodes - a node X in the tree is good if in the path from root to X there are no nodes with a value greater than X
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            #if the node is None, return 0
            if not node: return 0
            #return 1 (node is good) if the node value is greater than the max value, else 0 whic will mean that the node is not good
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            #return the sum of the left and right subtrees
            res += dfs(node.left, maxVal) 
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, float("-inf"))


    #--- BACKTRACKING ---
    #given an m x n grid of characters board and a string word, return true if word exists in the grid.
    #word can be constructed from letters of sequentially adjacent cell, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
    def wordExists(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, char):
            #if we finish the word, return True
            if char == len(word):
                return True
            #if the row or col is out of bounds, if the char is not the same as the board, or if we have already visited this path, return False
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or word[char] != board[row][col] or (row, col) in path):
                return False
            #add the current path to the path set
            path.add((row, col))
            #recursive call to the left, right, up and down
            res = dfs(row + 1, col, char + 1) or dfs(row - 1, col, char + 1) or dfs(row, col + 1, char + 1) or dfs(row, col - 1, char + 1)
            #remove the current path from the path set
            path.remove((row, col))
            return res

        #do the deep for search
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                
        #we didn't find the word, return False
        return False


    #given an array of nums, return all the possible permutations
    def permutations(self, nums: List[int]) -> List[List[int]]:
        res = []

        #base case
        if (len(nums) == 1):
            return [nums.copy()] #can return also [nums[:]] which is a bit faster

        #loop through the nums
        for i in range(len(nums)):
            #remove the current/first num from the nums
            n = nums.pop(0)
            #find the permutations of the remaining nums
            perms = self.permutations(nums)

            for p in perms:
                #add the current num to the front of each permutation
                p.append(n)
            #add the permutations to the result
            res.extend(perms)
            #add back the current num to the nums
            nums.append(n)

        return res    




    #given an integer array nums, return all possible subsets (the power set).
    #the solution set must not contain duplicate subsets.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            #if we finish the nums, add the subset to the result
            if i == len(nums):
                res.append(subset.copy())
                return

            #decision to include the current num in the subset
            subset.append(nums[i])
            #recursive call to the left and right
            dfs(i + 1)

            #decision to exclude the current num from the subset
            subset.pop()
            #recursive call to the left and right
            dfs(i + 1)

        dfs(0)
        return res


    #--- LINKED LIST ---
    def reorderList(self, head: ListNode) -> Optional[ListNode]:
        #pointers
        slow, fast = head, head.next
        #while the fast pointer is not None
        while fast and fast.next:
            #move the slow pointer to the next node
            slow = slow.next
            #move the fast pointer to the next node (jumps two nodes)
            fast = fast.next.next

        #get the middle or close to middle node
        #is going to be the next node to the current slow pointer position
        second = slow.next
        #set slow to Node
        prev = slow.next = None
        #we need to reverse the second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

    #merge two sorted linked lists and return it as a new sorted list
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #dummy list
        dummy = array_to_linked_list([None])
        tail = dummy

        #while the l1 and l2 pointers are not None
        while l1 and l2:
            #if the l1 value is less than the l2 value, add the l1 value to the tail
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:   
               #if the l1 value is greater than the l2 value, add the l2 value to the tail
                tail.next = l2
                l2 = l2.next
            #move the tail to the next node
            tail = tail.next

        #check if the l1 or l2 pointers are None
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        #return the dummy list
        return dummy.next



    #reverse a linked list
    def reverseList(self, head: ListNode) -> ListNode:
        #pointers
        prev, current = None, head
        #while the current pointer is not None
        while current:
            #move the current pointer to the next node
            tmp = current.next
            #move the current node to the prev pointer
            current.next = prev
            #set the prev pointer to the current node
            prev = current
            #set the current pointer to the next node
            current = tmp
        return prev



    #--- DYNAMIC PROGRAMMING ---
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #(index, totalSum) -> # of ways

        def backtrack(i, total):
            #if we reach the last index
            if i == len(nums):
                #if the total sum is equal to the target, return 1
                if total == target:
                    return 1
                else:
                    return 0
            #if we have already found the total sum, return the value from the dp (cache)
            if (i, total) in dp:
                return dp[(i, total)]

            #recursive call
            #will return the number of ways to reach the target sum
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))
         
            return dp[(i, total)]

        return backtrack(0, 0)


    #given a string s, find the longest palindromic substring in s
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l,r = i, i
            #check if the current substring is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #update the length if is the longest palindrome we have found
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                #expand the left and right
                l -= 1
                r += 1
                    
            #even length
            l,r = i, i + 1
            #check if the current substring is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #update the length if is the longest palindrome we have found
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                #expand the left and right
                l -= 1
                r += 1

        return res


    #a robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    # the robot can only move either down or right at any point in time.
    # the robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    # how many possible unique paths are there?
    def uniquePaths(self, m: int, n: int) -> int:
            row = [1] * n  #last row is always 1

            for i in range(m - 1): #m - 1 because we don't need to count the last row
                #create a new row
                #init the new row with 1
                newRow = [1] * n
                for j in range(n - 2, -1, -1): #moves from bottom to top
                    newRow[j] = newRow[j + 1] + row[j]
                row = newRow
            return row[0]




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

#input: root: [3, 1, 4, 3, null, 1, 5]
#output: 4
#Root Node: 3 (good)
root = creatBTree([3, 1, 4, 3, None, 1, 5], 0)
print(Solution().goodNodes(root))

#input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#output: True
#The word exists in the grid
print(Solution().wordExists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

#input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#output: False
#The word does not exist in the grid
print(Solution().wordExists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))

#input: nums = [1, 2, 3]
#output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#the power set of the array
print(Solution().subsets([1, 2, 3]))

#input: nums = [1, 2]
#output: [[], [1], [2], [1, 2]]
#the power set of the array
print(Solution().subsets([1, 2]))

#input: nums = [1, 2, 3]
#output: [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
#the permutations of the array
print(Solution().permutations([1, 2, 3]))

#input: nums = [1, 2]
#output: [[1, 2], [2, 1]]
#the permutations of the array
print(Solution().permutations([1, 2]))

#input: head = [1, 2, 3, 4]
#output: [1,4,2,3]
#reorder the linked list
my_array = [1, 2, 3, 4]
linked_list_head = array_to_linked_list(my_array)
print(Solution().reorderList(linked_list_head))


#input: 1 -> 2 -> 4, 1 -> 3 -> 4
#output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
my_array2 = [1, 2, 4]
my_array3 = [1, 3, 4]
linked_list_head_2 = array_to_linked_list(my_array2)
linked_list_head_3 = array_to_linked_list(my_array3)
print(Solution().mergeTwoLists(linked_list_head_2, linked_list_head_3))


#input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
#output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
my_array4 = [1, 2, 3, 4, 5, None]
linked_list_head_4 = array_to_linked_list(my_array4)
print(Solution().reverseList(linked_list_head_4))

#input: nums = [1,1,1,1,1], target = 3
#output: 5
#there are 5 ways to reach the target sum
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

#input: s = "babad"
#output: "bab" and also can be "aba"
print(Solution().longestPalindrome("babad"))

#input: "cbbd"
#outpu: "bb"
print(Solution().longestPalindrome("cbbd"))

#input: m = 3, n = 7
#output: 28
print(Solution().uniquePaths(3, 7))