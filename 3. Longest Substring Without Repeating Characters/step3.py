class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        longest_length = 0
        ascii_code_to_count = [0] * 256
        for end_index in range(len(s)):
            end_ascii_code = ord(s[end_index])
            while ascii_code_to_count[end_ascii_code] > 0:
                start_ascii_code = ord(s[start_index])
                ascii_code_to_count[start_ascii_code] -= 1
                start_index += 1
            longest_length = max(longest_length, end_index - start_index + 1)
            ascii_code_to_count[end_ascii_code] += 1
        return longest_length
