class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n, m = len(matrix), len(matrix[0])
        l = 0
        h = m * n-1

        while l <= h:
            mid = (l + h)//2
            mid_value = matrix=[mid//n][mid%n]

            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else: 
                h  = mid -1