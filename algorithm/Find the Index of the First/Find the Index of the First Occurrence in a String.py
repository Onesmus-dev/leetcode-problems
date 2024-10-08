class Solution():
    """in this solution we use the inbuild find method to search through the string and find the pattern.
    """
    def findstring(self,haystack, needle):
        if not needle: #check if the needle is empty
            return 0
        index = haystack.find(needle)#if not we call the find method to search for needle
        return index if index != -1 else -1 #the return checks if the index of the pattern and returns -1 if not found

