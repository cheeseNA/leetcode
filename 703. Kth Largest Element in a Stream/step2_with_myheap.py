class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.top_k_min_heap = MyHeap()
        self.k = k
        for num in nums:
            self.add(num)
        return

    def add(self, val: int) -> int:
        self.top_k_min_heap.push(val)
        while len(self.top_k_min_heap) > self.k:
            self.top_k_min_heap.pop()
        return self.top_k_min_heap.top()
