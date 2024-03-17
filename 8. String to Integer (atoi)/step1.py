class Solution:
    def clamp_to_32bit_signed(self, num: int) -> int:
        return max(-(2 ** 31), min(2 ** 31 - 1, num))

    def myAtoi(self, s: str) -> int:
        digits = "0123456789"
        number = 0
        is_positive = True
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and s[index] in "-+":
            if s[index] == "-":
                is_positive = False
            index += 1
        while index < len(s) and s[index] in digits:
            number *= 10
            number += int(s[index])
            index += 1
        number *= 1 if is_positive else -1
        return self.clamp_to_32bit_signed(number)
        