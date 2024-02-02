class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        # returning the sum of squared digits usingh this fuction
        def sumSquare(n):
            numlist = [0]
            sum =0
            #separating the digits using the while loop
            while n != 0:
                numlist.append(n%10)
                n = n//10
            
            # calculating the sum
            for i in numlist:
                sum += i**2
            
            return sum

    # Chceking if the number is happy
        while True:
            # getting the sum of the squared numbers
            n = sumSquare(n)
            # if the nuimber is 1 then happy
            if n == 1:
                return True
            # if not then check if the number is previously encountered indicating an infinite loop
            elif n in num:
                return False
            # otherwise add it to list of encountered numbers and move on to check the sum 
            else:
                num.add(n)
