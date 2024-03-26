from collections import defaultdict
import heapq
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        unique_nums = list(num_to_freq.keys())
        
        def swap(l: list, a: int, b: int):
            l[a], l[b] = l[b], l[a]
            return

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_value = num_to_freq[unique_nums[pivot_index]]
            store_index = left
            swap(unique_nums, pivot_index, right - 1)
            for i in range(left, right - 1):
                if num_to_freq[unique_nums[i]] > pivot_value:
                    swap(unique_nums, i, store_index)
                    store_index += 1
            swap(unique_nums, right - 1, store_index)
            return store_index
        
        def quick_select(left: int, right: int, k: int):
            if right <= left + 1:
                return
            pivot_index = random.randint(left, right - 1)
            selected_index = partition(left, right, pivot_index)
            if selected_index == k:
                return
            elif selected_index < k:
                quick_select(selected_index + 1, right, k)
            else:
                quick_select(left, selected_index, k)
            return

        quick_select(0, len(unique_nums), k)
        return unique_nums[:k]