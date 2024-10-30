# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        ans = []
        for i in range(m):
            lst = []
            for j in range(n):
                count = self.ct(board, i, j)
                if board[i][j] == 0:
                    if count == 3:
                        lst.append(1)
                    else:
                        lst.append(0)
                elif board[i][j] == 1:
                    if count > 3 or count < 2:
                        lst.append(0)
                    else:
                        lst.append(1)
            ans.append(lst)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = ans[i][j]

    def ct(self, board, m, n):
        edge1 = len(board)
        edge2 = len(board[0])
        if m - 1 < 0:
            up = 0
        else:
            up = m - 1
        if n + 1 == edge2:
            right = n + 1
        else:
            right = n + 2
        if m + 1 == edge1:
            down = m + 1 
        else:
            down = m + 2
        if n - 1 < 0:
            left = 0
        else:
            left = n - 1
        count = 0
        for i in range(up, down):
            for j in range(left, right):
                if i != m or j != n:
                    if board[i][j] == 1:
                        count += 1
        return count

# in this program, I use ct funtion to count the number of 1 surround the target element
# in the ct function, it judgement the area where neer to be counting, because the properties of list, if the element is not at the edge of the matrix, you need to set the range + 1,
# which means, if the selected number was matrix[1][1], so the top should be 0, bottom should be 3, left should be 0, right should be 3
