class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_stack = []
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in open_to_close:
                open_bracket_stack.append(char)
                continue
            if not open_bracket_stack:
                return False
            if char != open_to_close[open_bracket_stack[-1]]:
                return False
            open_bracket_stack.pop()
        if len(open_bracket_stack) > 0:
            return False
        return True

