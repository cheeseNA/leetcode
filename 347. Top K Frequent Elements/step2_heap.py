from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        heap = []
        for num, freq in num_to_freq.items():
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap)
        top_k_nums = [num for freq, num in heap]
        return top_k_nums