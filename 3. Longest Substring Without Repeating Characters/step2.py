class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        char_to_last_appeared_index = {}
        max_length = 0
        for right_index, char in enumerate(s):
            if char in char_to_last_appeared_index:
                left_index = max(left_index, char_to_last_appeared_index[char] + 1)
            char_to_last_appeared_index[char] = right_index
            max_length = max(max_length, right_index - left_index + 1)
        return max_length
