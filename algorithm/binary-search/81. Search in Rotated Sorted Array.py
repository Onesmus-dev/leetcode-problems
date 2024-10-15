class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        """There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums."""
        
        l, h = 0, len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            # If target is found, return True
            if nums[mid] == target:
                return True
            
            # Handle duplicates: If the values at l, mid, and h are the same, shrink the search space
            if nums[l] == nums[mid] == nums[h]:
                l += 1
                h -= 1
            # Left half is sorted
            elif nums[l] <= nums[mid]:
                # Check if the target is within the left sorted part
                if nums[l] <= target < nums[mid]:
                    h = mid - 1  # Move to the left half
                else:
                    l = mid + 1  # Move to the right half
            # Right half is sorted
            else:
                # Check if the target is within the right sorted part
                if nums[mid] < target <= nums[h]:
                    l = mid + 1  # Move to the right half
                else:
                    h = mid - 1  # Move to the left half
        
        return False  # Target not found
