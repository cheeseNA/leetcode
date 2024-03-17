class Solution:
    def myAtoi(self, s: str) -> int:
        upper_bound = 2 ** 31 - 1
        lower_bound = -1 * (2 ** 31)

        if s == "":
            return 0
        
        length = len(s)
        cursor = 0
        while cursor < length and s[cursor] == " ":
            cursor += 1
        if cursor == length:
            return 0

        is_positive = True
        if s[cursor] == "-":
            is_positive = False
            cursor += 1
        elif s[cursor] == "+":
            cursor += 1
        if cursor == length:
            # when no digits were read
            return 0
        
        abs_value = 0
        while cursor < length and '0' <= s[cursor] <= '9':
            abs_value *= 10
            abs_value += ord(s[cursor]) - ord('0')
            cursor += 1
        signed_value = abs_value if is_positive else -1 * abs_value
        if signed_value > upper_bound:
            signed_value = upper_bound
        if signed_value < lower_bound:
            signed_value = lower_bound
        return signed_value