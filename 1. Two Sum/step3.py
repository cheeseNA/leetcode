class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_num_to_index = {}
        for index, num in enumerate(nums):
            complement_num = target - num
            if complement_num in appeared_num_to_index:
                return [index, appeared_num_to_index[complement_num]]
            appeared_num_to_index[num] = index
        return []
