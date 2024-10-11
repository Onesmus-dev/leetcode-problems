"""Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2)."""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        l, h = matrix[0][0], matrix[n-1][n-1]
        
        while l < h:
            mid = (l + h) // 2
            count = 0
            j = n - 1
            
            # Count elements less than or equal to mid
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            
            if count < k:
                l = mid + 1
            else:
                h = mid
        
        return l
