class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def helper(dg):
            if len(dg) == 0:
                return ""
            output = []
            if len(dg) == 1:
                for i in keypad[dg[0]]:
                    output.append(i)
            
            for i in keypad[dg[0]]:
                for x in helper(dg[1:]):
                    output.append(i + x)
            return output
        return helper(digits)
