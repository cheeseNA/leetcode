class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        longest_length = 1
        start_index = 0
        end_index = 0
        appeared_chars = set(s[0])
        while True:
            while end_index + 1 < length and s[end_index + 1] not in appeared_chars:
                end_index += 1
                appeared_chars.add(s[end_index])
            # print("#", start_index, end_index)
            if end_index == length - 1:
                return max(longest_length, end_index - start_index + 1)
            longest_length = max(longest_length, end_index - start_index + 1)
            while s[start_index] != s[end_index + 1]:
                # print(start_index, end_index)
                appeared_chars.remove(s[start_index])
                start_index += 1
            appeared_chars.remove(s[start_index])
            start_index += 1
            