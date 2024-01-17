class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        
        for word in strs[1:]:
            print(pre)
            print(word)
            for ind,ch in enumerate(pre):
                print(ind)
                if(ind < len(word)):
                    if (pre[ind] == word[ind]):
                        continue
                    else:
                        print('here')
                        pre = pre[:ind]
                        break
                else:
                    pre = pre[:len(word)]
        return pre

            
        