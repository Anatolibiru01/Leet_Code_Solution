class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in matching:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if matching[top] != char:
                    return False
        return not stack
