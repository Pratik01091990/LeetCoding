class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = []
        s = ''.join([i.lower() for i in s if i.isalnum()])
        
        l = 0
        
        for r in range(len(s)-1,0,-1):
            if s[l] != s[r]:
                return False
            else:
                l += 1
        
        return True
