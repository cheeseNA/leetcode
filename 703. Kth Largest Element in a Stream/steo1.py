from heapq import heapify, heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        sorted_nums = sorted(nums, reverse=True)
        self.top_k_min_heap = sorted_nums[:k]
        heapify(self.top_k_min_heap)
        self.k = k
        return

    def add(self, val: int) -> int:
        heappush(self.top_k_min_heap, val)
        while len(self.top_k_min_heap) > self.k:
            heappop(self.top_k_min_heap)
        kth_num = self.top_k_min_heap[0]
        return kth_num


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
