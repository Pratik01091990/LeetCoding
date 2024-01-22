class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in ransomNote:
            cont = False   
            for j in magazine:
                
                if i == j:
                    cont = True
                    magazine.remove(j)
                    break
            
            if cont == False:
                return False
            
        return True
