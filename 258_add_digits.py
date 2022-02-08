class Solution:
    def addDigits(self, num: int) -> int:
        if num%9!= 0: 
            return(num%9)
        elif num == 0: 
            return(0)
        elif num%9 == 0: 
            return(9)