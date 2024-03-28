from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_stack = deque()
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        open_brackets = close_to_open.values()
        for char in s:
            if char in open_brackets:
                open_bracket_stack.append(char)
            else:
                if len(open_bracket_stack) == 0:
                    return False
                if open_bracket_stack.pop() != close_to_open[char]:
                    return False
        return len(open_bracket_stack) == 0
