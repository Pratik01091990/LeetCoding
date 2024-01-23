class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) -1
        digits[last] = digits[last] +1
        #print(digits)
        result = []
        if (digits[last] > 9):
            
            if(digits[0] >= 9):
                digits.reverse()
                digits.append(0)
                digits.reverse()
                last += 1
                
            for i in range(last, -1,-1):
                
                carry = digits[i]//10
                digits[i] = digits[i]%10
                if carry == 0:
                    break
                digits[i-1] = digits[i-1] + carry
            
            if digits[0] == 0:
                digits.remove(digits[0])
            
            return digits
        
        else:
            return digits

        
        


        