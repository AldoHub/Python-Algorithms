#--- TWO POINTERS ---
#use two pointers pattern when you face problems like: PALINDROMES, REVERSALS, MERGING SORTED DATA, "K" SIZED COMPARISONS


#--- valid palindrome ---
# Given a string s determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def is_palindrome(s: str) -> bool:
    #pointers
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        #lowercase the chars and check if they are equal
        if s[left].lower() != s[right].lower():
            return False
        #move the pointers
        left += 1
        right -= 1
        #if all the chars are equal, return True - the string is a palindrome
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))


#--- middle of the linked list ---
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.


class Node: 
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def middleNode(head: Node) -> int:
    #pointers - slow and fast
    slow, fast = head, head #both start at the head
    #while the fast pointer is not None - meaning is at the end of the list
    while fast and fast.next:
        #move the slow pointer to the next node
        slow = slow.next
        #move the fast pointer to the next node (jumps two nodes)
        fast = fast.next.next

    return slow.val #return the slow pointer - which will be at the middle node once the fast pointer is None