class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_index = 0
        current_index = 0

        for i in s:
            found = False
            for j in range(0, len(t)):
                if (i == t[j]):
                    #prev_index = j
                    t = t[j+1:]
                    found = True
                    break
            
            if(found != True):
                return False
        
        return True