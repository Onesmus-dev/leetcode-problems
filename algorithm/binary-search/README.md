153. Find Minimum in Rotated Sorted Array
My intial thinking was.
1.Create a new array: You planned to create a new array (nums2) and sort it. This would give you the original sorted array before rotation.
2.Compare nums[0] with the sorted array: You wanted to compare nums[0] with the sorted array to determine how many rotations were made by finding its position in the sorted array.
3.Find the number of rotations: You intended to calculate the number of rotations based on where nums[0] appears in the sorted array.

The trick in this problem is that the question requires us to find the minimum number not number of rotations.

So the correct thinking is:
1.Directly Find the Minimum Element: Instead of sorting or creating a new array, use binary search to narrow down the part of the array where the minimum element resides. This is possible because one part of the array is always sorted, and you can compare elements to determine which half contains the minimum.
2.Modified Binary Search: Rather than using nums2[mid] < nums[0], compare elements like nums[mid] > nums[high] to determine if the minimum is in the right half or left half.