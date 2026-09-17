#--- DEPTH-FIRST SEARCH (DFS) ---

# DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking.
# DFS can be used to traverse or search a graph or tree. It starts at some root node and explores as far as possible along each branch before backtracking.

# DFS is a recursive algorithm and uses a stack data structure to store the nodes to be explored. It starts by pushing the root node onto the stack and then repeatedly pops a node, visits it, and pushes its unvisited neighbors onto the stack.
# DFS is often implemented using a recursive function that takes a node as input and returns a list of visited nodes.

#--- Maximum Depth of a Binary Tree ---

# given the root of a binary tree, return its maximum depth

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


def tree_max_depth(root: TreeNode) -> int:
    def dfs(root):
        #if the root is None, return 0
        if not root: return 0
        #return the max depth of the left and right subtrees - we do a recursive call to the left and right subtrees
        return max(dfs(root.left), dfs(root.right)) + 1 #+1 because we need to count the root node

    return dfs(root) - 1 if root else 0


#output: 3
print(tree_max_depth(creatBTree([3, 9, 20, None, None, 15, 7], 0)))


#--- Number of Islands---

# given an m x n grid consisting og 1s (land) and 0s (water), return the number of islands

def numIslands(grid: List[List[int]]) -> int:
    #get rows and cols
    rows, cols = len(grid), len(grid[0])

    #get the adjacent cells
    def get_neighbors(coord):
        res = []
        row, col = coord
        deltaRow = [-1, 0, 1, 0]
        deltaCol = [0, 1, 0, -1]
        for i in range(len(deltaRow)):
            r = row + deltaRow[i]
            c = col + deltaCol[i]
            if r >= 0 and r < rows and c >= 0 and c < cols:
                res.append((r, c))
        return res

    def dfs(coord):
        row, col = coord
        if grid[row][col] == 0:
            return

        #if its not water, set it to water and explore the neighbors
        grid[row][col] = 0
        for neighbor in get_neighbors(coord):
            nr, nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs((r, c))
                count += 1

    return count

#input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
#output: 1
print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

#input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
#output: 3
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

#input: grid = [["1","1","1","0","0"],["1","1","0","1","1"],["1","1","0","0","0"],["0","0","0","0","0
