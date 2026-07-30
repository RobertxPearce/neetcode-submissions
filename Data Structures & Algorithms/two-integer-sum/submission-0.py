class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            target_diff = target - num

            if target_diff in num_dict:
                return [num_dict[target_diff], i]
            
            num_dict[num] = i
            