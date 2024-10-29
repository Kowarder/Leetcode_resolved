# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# this is using revise the matrix and then exchange symmetrical elements to get the final result
# to ensure exchange each element without over exchange, using first loop range(n) and second loop range(i) to ensure that all elements in the lower trangle has been iterated.

# at first i tried using an extra matrix to store the result and assigning this to the original matrix like matrix = ans, but it seems not works through the leetcode test
# it needs to change the matrix itself
