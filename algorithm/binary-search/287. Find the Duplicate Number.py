class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            count = sum(num <= mid for num in nums)#Count how many numbers are less than or equal to mid using a generator expression.
            
            if count > mid:
                right = mid  # Duplicate is in the left half
            else:
                left = mid + 1  # Duplicate is in the right half
        
        return left