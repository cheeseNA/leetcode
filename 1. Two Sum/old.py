class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        num_indexes = [(nums[i], i) for i in range(length)]
        sorted_num_indexes = sorted(num_indexes)
        small_idx = 0
        large_idx = length - 1
        while small_idx < large_idx:
            temporary_sum = sorted_num_indexes[small_idx][0] + sorted_num_indexes[large_idx][0]
            if temporary_sum == target:
                return [sorted_num_indexes[small_idx][1], sorted_num_indexes[large_idx][1]]
            elif temporary_sum < target:
                small_idx += 1
            else:
                large_idx -= 1
        raise Error

        