class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum = ""
        for i in range(len(s)):
            s1 = expandFromCenter(s, i, i)
            s2 = expandFromCenter(s, i, i + 1)
            
            if len(s1) >= len(s2) and len(s1) > len(maximum):
                maximum = s1
            elif len(s2) > len(maximum):
                maximum = s2
                
        return maximum
    
def expandFromCenter(s, left, right):
    if s is None or left > right:
        return ""

    while(0 <= left and right < len(s) and s[left] == s[right]):
        left -=1
        right +=1
    return s[left+1:right]
