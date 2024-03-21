class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        chars_for_each_row = [[] for _ in range(numRows)]
        index = 0
        while index < len(s):
            for row in range(numRows - 1):
                if index >= len(s):
                    break
                chars_for_each_row[row].append(s[index])
                index += 1
            for row in range(numRows - 1, 0, -1):
                if index >= len(s):
                    break
                chars_for_each_row[row].append(s[index])
                index += 1
        string_for_each_row = ["".join(chars) for chars in chars_for_each_row]
        return "".join(string_for_each_row)
                