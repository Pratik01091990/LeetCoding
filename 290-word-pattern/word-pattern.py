class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordlst = s.split()
        pat = {}
        #pat2 = {}
        # check the lenghts
        if (len(pattern) != len(wordlst)):
            return False
        
        for h,i in enumerate(pattern):
            #print(pat)
            if (i not in pat.keys()) and (wordlst[h] not in pat.values()):
                pat[i] = wordlst[h]
            elif(i in pat.keys()) and (wordlst[h] == pat[i]):
                continue
            else:
                return False

        
        return True


            

        