class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1,n+1):
            app = ''
            if i%15 == 0:
                app = "FizzBuzz"
            elif i%5 == 0:
                app = "Buzz"
            elif i%3 == 0:
                app = "Fizz"
            else:
                app = str(i)
            ret.append(app)
        
        return ret