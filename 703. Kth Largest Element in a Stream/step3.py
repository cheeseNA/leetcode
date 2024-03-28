import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self._top_k_heap = []
        self._k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self._top_k_heap, val)
        while len(self._top_k_heap) > self._k:
            heapq.heappop(self._top_k_heap)
        return self._top_k_heap[0]