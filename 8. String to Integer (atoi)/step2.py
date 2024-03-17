class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_VALUE = -1 * (2 ** 31)
        MAX_VALUE = 2 ** 31 - 1
        abs_value = 0
        is_positive = True
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        
        if index < len(s) and s[index] in "-+":
            if s[index] == "-":
                is_positive = False
            index += 1
        
        while index < len(s) and "0" <= s[index] <= "9":
            digit = int(s[index])
            abs_value *= 10
            abs_value += digit
            index += 1
            if is_positive and abs_value >= MAX_VALUE:
                return MAX_VALUE
            if (not is_positive) and abs_value * -1 <= MIN_VALUE:
                return MIN_VALUE
        return abs_value * (1 if is_positive else -1)
