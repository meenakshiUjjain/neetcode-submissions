class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in out:
                return [out[diff], i]
            out[num] = i
        