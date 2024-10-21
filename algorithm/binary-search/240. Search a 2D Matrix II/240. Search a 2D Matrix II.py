class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        

        n = len(matrix)
        m = len(matrix[0])
        r = n-1
        c = 0

        while r >=0  and c < m:
            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                c +=1
            else:
                r -=1
        return False
            
        