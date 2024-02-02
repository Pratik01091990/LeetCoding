class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        def sumSquare(n):
            numlist = [0]
            sum =0
            #i = 0
            while n != 0:
                numlist.append(n%10)
                n = n//10
                
            
            for i in numlist:
                sum += i**2
            
            return sum


        while True:
            n = sumSquare(n)
            if n == 1:
                return True
            elif n in num:
                return False
            else:
                num.add(n)
