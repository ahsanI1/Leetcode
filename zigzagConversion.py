class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans_array = []
        
        for i in range(numRows):
            ans_array.append("")
            
        goingDown = True
        index = 0
        for i in s:
            ans_array[index] += i
            
            if index >= numRows - 1:
                goingDown = False
            elif index <= 0:
                goingDown = True
            
            if goingDown:
                index+=1
            else:
                index-=1
                
        ans = ""
        for i in ans_array:
            ans += i
        return ans
