class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        backtrack(ans, "", 0, 0, n)
        return ans
    
def backtrack(ans, curr_string, opn, close, n):
    if len(curr_string) == n * 2:
        ans.append(curr_string)
        return None
    if opn < n:
        backtrack(ans, curr_string + "(", opn + 1, close, n)
    if close < opn:
        backtrack(ans, curr_string + ")", opn, close + 1, n)
