class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        result = 0
        for r in range(0,len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l = l + 1
            charset.add(s[r])
            result = max(result,len(charset))
        
        return result
        
          
# Solution by NeetCode