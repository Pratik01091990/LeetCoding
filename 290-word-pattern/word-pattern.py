class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordlst = s.split()
        pat = {}

        # check the lenghts if not same then return fasle
        if (len(pattern) != len(wordlst)):
            return False

        # check the character is in the pattern and the word is mapped to the pattern        
        for h,i in enumerate(pattern):
            # if the character and pattern not in the dictionary then map the word
            if (i not in pat.keys()) and (wordlst[h] not in pat.values()):
                pat[i] = wordlst[h]
            # if the character is present and mapped to the correct word then continue checking
            elif(i in pat.keys()) and (wordlst[h] == pat[i]):
                continue
            # if the above conditions fail then the character is in the dictionary and mapped to a different word 
            else:
                return False

        # if the control flow is here then retunrn true
        return True


            

        