class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        open_bracket_stack = []
        for char in s:
            if char in open_to_close:
                open_bracket_stack.append(char)
                continue
            if not open_bracket_stack:
                return False
            recent_open_bracket = open_bracket_stack.pop()
            if open_to_close[recent_open_bracket] != char:
                return False
        return not open_bracket_stack
