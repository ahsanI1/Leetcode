class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            minindex = min(len(prefix), len(strs[i]))
            x = 0
            while(x < minindex and prefix[x] == strs[i][x]):
                x+=1
            prefix = prefix[:x]
        return prefix
