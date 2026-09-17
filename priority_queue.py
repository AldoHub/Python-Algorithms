#--- PRIORITY QUEUE ---
# a priority queue is a data structure that stores elements in a queue and orders them according to their priority.
# the priority of an element is determined by a function that maps the element to a value.
# the element with the highest priority is dequeued first.

# a priority queue is implemented using a heap data structure, where each element is stored as a tuple (priority, element).
# the heap is implemented using an array, where the parent-child relationship is determined by the priority of the element.
# the left child of an element is at index 2 * i + 1 and the right child is at index 2 * i + 2.

#--- K Closest Points to Origin ---

# given a set of points in the plane, and a positive integer k, find the k closest points to the origin (0, 0).

from heapq import heapify, heappush, heappop
from typing import List

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = x ** 2 + y ** 2

    def __lt__(self, other):
        return self.distance < other.distance
    
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    #create the heap - keep track of the distance and the point
    heap: list[tuple[int, list[int]]] = []

    #loop through the points
    for point in points:
        #add the point to the heap
        heappush(heap, (point[0] ** 2 + point[1] ** 2, point))

    res = []
    for _ in range(k):
        _, point = heappop(heap)
        res.append(point)

    return res

#input: points = [[1,3],[-2,2]], k = 1
#output: [[-2,2]]
print(k_closest([[1,3],[-2,2]], 1))

#--- Kth largest element in an array ---

# find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

def find_kth_largest(nums: list[int], k: int) -> int:
    #get all the elements and negate them
    nums = [-x for x in nums]
    heapify(nums)

    #loop through the nums
    for _ in range(k - 1):
        heappop(nums)

    return -nums[0] #flip again the number to return the original value

print(find_kth_largest([4, 5, 8, 2], 2)) #output: 8
print(find_kth_largest([1, 2, 3, 4], 3)) #output: 4