#--- BINARY SEARCH---

#--- find the First True in a sorted boolean array ---

# an array of boolean values is divided into two sections: The left section consists of all false, and the right section consists of all true.
# find the first true value in the right section of the array.
# if no true value exists, return -1.

def find_boundary(nums: list[bool]) -> int:
    #set the pointers
    left, right = 0, len(nums) - 1
    #init the boundary index
    boundary_index = -1

    while left <= right:
        #get the middle index
        mid = (left + right) // 2
        #if the middle index is true, update the boundary index
        if nums[mid]:
            boundary_index = mid
            #move the right pointer in order to see if there is a better boundary
            right = mid - 1
        else:
            #the index is invalid, move to the left
            left = mid + 1

    return boundary_index

print(find_boundary([False, False, True, True, True, False, False]))


#--- find Minimum in Rotated Sorted Array ---             

# A sorted array is rotated at some pivot unknown to you beforehand. For example the array [10, 20, 30, 40, 50] might become [30, 40, 50, 10, 20].
# find the index of the minimum element in the rotated array.


def find_min_rotated(nums: list[int]) -> int:
    #set the pointers
    left, right = 0, len(nums) - 1
    #init the boundary index
    boundary_index = -1

    while left <= right:
        #get the middle index
        mid = (left + right) // 2
        #check if the index is less or equal to the pivot - last item in the index
        if nums[mid] <= nums[-1]:
            boundary_index = mid
            #move the right pointer in order to see if there is a better boundary
            right = mid - 1
        else:
            #the index is invalid, move to the left
            left = mid + 1

    return boundary_index

print(find_min_rotated([30, 40, 50, 10, 20])) #output: 10 is the min and index is 3
print(find_min_rotated([3, 5, 7, 11, 13, 17, 19, 2])) #output: 2 is the min and 7 is the index
