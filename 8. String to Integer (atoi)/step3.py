class Solution:
    def myAtoi(self, s: str) -> int:
        UPPER_BOUND = 2 ** 31 - 1
        LOWER_BOUND = -(2 ** 31)
        index = 0
        is_positive = True
        abs_value = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                is_positive = False
            index += 1
        while index < len(s) and s[index].isdigit():
            abs_value *= 10
            abs_value += int(s[index])
            if is_positive and abs_value >= UPPER_BOUND:
                return UPPER_BOUND
            if not is_positive and -1 * abs_value <= LOWER_BOUND:
                return LOWER_BOUND
            index += 1
        return abs_value * (1 if is_positive else -1)