#--- BREADTH-FIRST SEARCH (BFS) ---

# BFS is a graph traversal algorithm that starts at a given node and explores all of the neighboring nodes at the present depth prior to moving on to nodes at the next depth level.
# BFS can be used to traverse or search a graph or tree. It starts at some root node and explores as far as possible along each branch before backtracking.

# BFS is a recursive algorithm and uses a queue data structure to store the nodes to be explored. It starts by enqueueing the root node and then repeatedly dequeues a node, visits it, and enqueues its unvisited neighbors.
# BFS is often implemented using a recursive function that takes a node as input and returns a list of visited nodes.

#--- Bynary tree level order traversal ---

# given a binary tree, return the level order traversal of its nodes' values.

from collections import deque
from typing import List

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


def level_order_traversal(root: TreeNode) -> List[List[int]]:
    #define an empty list to store the nodes
    res = []
    #init the queue
    queue = deque([root])
    #while the queue is not empty
    while len(queue) > 0:
        #get the lenght of the current level
        n = len(queue)
        #init the new level
        new_level = []

        #loop through the current level
        for i in range(n):
            #get the current node
            node = queue.popleft()
            #add the current node to the new level
            new_level.append(node.val)

            for child in [node.left, node.right]:
                if child is not None:
                    #add the child to the queue
                    queue.append(child)
        #add the new level to the result
        res.append(new_level)
    return res


print(level_order_traversal(creatBTree([3, 9, 20, None, None, 15, 7], 0)))

