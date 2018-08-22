__author__ = 'yulin'
'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class SAM(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix)-1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False


def main():
    sam = SAM()
    max = list([list([1, 4, 7, 11, 15]), list([2, 5, 8, 12, 19]), list([3, 6, 9, 16, 22]), list([10, 13, 14, 17, 24]),
                list([18, 21, 23, 26, 30])])
    print(sam.searchMatrix(max, 5))


if __name__ == '__main__':
    main()
