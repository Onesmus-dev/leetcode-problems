class Solution:
    def prefix_search(self, pattern, m, prefix_array):
        length = 0
        prefix_array[0] = 0  # The first element is always 0
        i = 1
        
        # Build the prefix array (Longest Prefix Suffix - LPS)
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                prefix_array[i] = length
                i += 1
            else:
                if length != 0:
                    length = prefix_array[length - 1]
                else:
                    prefix_array[i] = 0
                    i += 1

    def strStr(self, haystack, needle):
        if not needle:  # If needle is empty, return 0
            return 0
        
        n = len(haystack)
        m = len(needle)
        
        # Edge case: if needle is longer than haystack
        if m > n:
            return -1
        
        # Step 1: Create the prefix (LPS) array
        prefix_array = [0] * m
        self.prefix_search(needle, m, prefix_array)
        
        # Step 2: Start matching haystack with the needle
        i = 0  # index for haystack
        j = 0  # index for needle
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m:  # If full pattern matched
                return i - j  # Return the starting index of the match
            
            # Mismatch after j matches
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = prefix_array[j - 1]  # Use the prefix array to avoid unnecessary comparisons
                else:
                    i += 1  # Move to the next character in haystack
        
        return -1  # No match found
