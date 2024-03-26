from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        top_k_freq_heap = []
        for num, freq in num_counter.items():
            heapq.heappush(top_k_freq_heap, (freq, num))
            if len(top_k_freq_heap) > k:
                heapq.heappop(top_k_freq_heap)
        top_k_freq_nums = [num for freq, num in top_k_freq_heap]
        return top_k_freq_nums