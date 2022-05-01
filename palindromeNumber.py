class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rvrse = 0
        y = x
        while(y != 0):
            rvrse = rvrse * 10 + y %10
            y = math.floor(y/10)
            
        return x == rvrse
