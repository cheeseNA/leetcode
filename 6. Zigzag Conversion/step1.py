class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        string_for_each_row = [""] * numRows
        block_size = 2 * numRows - 2
        for index, char in enumerate(s):
            position_in_block = index % block_size
            if position_in_block < numRows - 1:
                string_for_each_row[position_in_block] += char
            else:
                string_for_each_row[block_size - position_in_block] += char
        return "".join(string_for_each_row)
                