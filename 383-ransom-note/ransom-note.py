class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #magazine = list(magazine)
        dic_ran = {}
        dic_mag = {}
        for i in ransomNote:
            if i not in dic_ran.keys():
                dic_ran[i] = ransomNote.count(i)
        
        for i in magazine:
            if i not in dic_mag.keys():
                dic_mag[i] = magazine.count(i)

        for i in dic_ran.keys():
            try:
                if dic_ran[i] <= dic_mag[i]:
                    continue
                else:
                    return False
            except KeyError:
                return False
        
        return True

