class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        
        for word in strs[1:]:

            for ind,ch in enumerate(pre):
                if(ind < len(word)):
                    if (pre[ind] == word[ind]):
                        continue
                    else:
                        pre = pre[:ind]
                        break
                else:
                    pre = pre[:len(word)]
        return pre

            
        