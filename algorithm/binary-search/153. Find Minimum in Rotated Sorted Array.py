class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize two pointers
        low, high = 0, len(nums) - 1
        
        # If the array is not rotated, the smallest element is the first element
        if nums[low] < nums[high]:
            return nums[low]
        
        # Perform binary search
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the high element,
            # the smallest value is in the right half of the array
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Otherwise, the smallest value is in the left half (or could be mid)
                high = mid
        
        # At the end of the binary search, low == high, pointing to the minimum element
        return nums[low]
