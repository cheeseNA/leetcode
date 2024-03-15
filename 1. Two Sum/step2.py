class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_number_to_index = {}
        for index, num in enumerate(nums):
            if target - num in appeared_number_to_index:
                return [index, appeared_number_to_index[target - num]]
            appeared_number_to_index[num] = index
        return []
