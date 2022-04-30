class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        y=x
        if y < 0:
            sign = -1
            y *= -1
        else:
            sign = 1
        while(y != 0):
            pos = y %10
            y = math.floor(y / 10)
            ans = ans * 10 + pos

        ans = ans * sign
        if x > 0:
            return ans if ans < 2**31 else 0
        return ans if ans > - 2**31 else 0
