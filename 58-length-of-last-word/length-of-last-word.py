class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lst = s.split(' ')
        print(lst)
        for i in range(len(lst) -1,-1,-1):
            print(i)
            l = len(lst[i])
            if (l !=0):
                return l
        return len(s)
