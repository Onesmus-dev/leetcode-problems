class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 0
        h = len(arr) - 1
        
        # Binary search for the peak
        while l < h:
            mid = (l + h) // 2
            
            # If middle element is less than the next one, peak is on the right
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            # Else, peak is on the left or at mid
            else:
                h = mid
        
        # When loop ends, l == h and this is the peak index
        return l
