class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif x == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif x == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif x == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
