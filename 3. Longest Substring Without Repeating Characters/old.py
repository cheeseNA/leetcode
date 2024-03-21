class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start_pos = 0
        end_pos = 0
        exist_set = {s[0]}
        answer = 1
        while end_pos < len(s) - 1:
            if s[end_pos + 1] not in exist_set:
                end_pos += 1
                exist_set.add(s[end_pos])
                answer = max(answer, end_pos - start_pos + 1)
            else:
                exist_set.remove(s[start_pos])
                if start_pos == end_pos:
                    start_pos = start_pos + 1
                    end_pos = start_pos
                    exist_set.add(s[start_pos])
                else:
                    start_pos = start_pos + 1
        return answer
