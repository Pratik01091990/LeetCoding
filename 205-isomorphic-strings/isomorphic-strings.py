class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charmapst = {}
        charmapts = {}
        if len(s) != len(t):
            return False
        else:
            for i,j in zip(s,t):
                if ((i in charmapst and charmapst[i] != j) or 
                    (j in charmapts and charmapts[j] != i)):
                    return False

                charmapst[i] = j
                charmapts[j] = i
            
        return True