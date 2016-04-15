"""
[ref.href] www.lintcode.com/en/problem/search-a-2d-matrix-ii
"
  Search a 2D Matrix II.
  
  Write an efficient algorithm that searches for a value in an 
  m * n matrix, return the occurrence of it.
  
  This matrix has the following properties:
  	Integers in each row are sorted from left to right.
  	Integers in each column are sorted from up to bottom.
  	No duplicate integers in each row or column.
  
  For example, given:
  
  [
    [1, 3, 5, 7],
    [2, 4, 7, 8],
    [3, 5, 9, 10]
  ]
  
  target = 3, return 2
"
"""

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if matrix == None:
            raise TypeError("matrix expected")
        
        rows = len(matrix)
        if rows < 1:
            return 0
            #raise ValueError("matrix should have at least one row")
            
        cols = len(matrix[0])
        if cols < 1:
            return 0
            #raise ValueError("matrix should have at least one col")
        
        count = 0
        row = rows - 1
        col = 0
        while row >= 0 and col < cols:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
                col += 1
                count += 1
        return count
