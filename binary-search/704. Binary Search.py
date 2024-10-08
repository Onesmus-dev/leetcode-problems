"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        u = len(nums) - 1

        while l <= u:
            mid = (l + u) // 2

            if nums[mid] == target:
                return mid  # Return the index if the target is found
            elif nums[mid] < target:
                l = mid + 1  # Move the lower bound up
            else:
                u = mid - 1  # Move the upper bound down

        return -1  # Return -1 if the target is not found
