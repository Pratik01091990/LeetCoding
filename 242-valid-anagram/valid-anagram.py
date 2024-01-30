class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #convert the strings to lists to use sort
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        # Check if the lengths are same if not then the words are not anagrams
        if len(s) != len(t):
            return False
        # If the lengths are equal, check charecter by character if the characters are unequal then return false
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        # if the control flow reaches here then the words are anagrams
        return True