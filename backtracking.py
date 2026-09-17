#--- BACKTRACKING ---

# BACKTRACKING is a general algorithm for finding all (or some) solutions to some computational problem.
# BACKTRACKING is a recursive algorithm and uses a stack data structure to store the nodes to be explored. It starts by pushing the root node onto the stack and then repeatedly pops a node, visits it, and pushes its unvisited neighbors onto the stack.
# BACKTRACKING is often implemented using a recursive function that takes a node as input and returns a list of visited nodes.

#--- Word Search ---
from typing import List


def exist_word(board: List[List[str]], word: str) -> bool:

    def dfs(row, col, char):

        if board[row][col] != word[char]:
            return False
        #if we finish the word, return True
        if char == len(word):
            return True

        #set the current coords
        char = board[row][col]
        #mark the current char as visited
        board[row][col] = "#"
        #recursive call to the left, right, up and down
        coords = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for r, c in coords:
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                if dfs(r, c, char + 1):
                    return True

        #reset the current char
        board[row][col] = char
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True
    return False

#input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#output: True
print(exist_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

#input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#output: False
print(exist_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))