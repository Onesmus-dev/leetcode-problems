class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        Binary Search: We maintain two pointers, l (left) and h (high), to search through the letters list.
Midpoint Calculation: In each iteration, we calculate the midpoint.
Comparison:
If the character at mid is less than or equal to the target since it already sorted, it means we need to search in the right half (so we move l to mid + 1).
If the character at mid is greater than the target, we search in the left half (so we move h to mid - 1).
Finding the Result: After the loop, if l exceeds the bounds of the list, we wrap around using l % len(letters) to get the first character.
        """
        l, h = 0, len(letters) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            # If the middle character is less than or equal to the target, search in the right half
            if letters[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        
        # If l is out of bounds, return the first character
        return letters[l % len(letters)]