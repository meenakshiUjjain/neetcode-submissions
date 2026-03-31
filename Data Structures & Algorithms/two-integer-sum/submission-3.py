class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resu = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in resu:
                return [resu[diff], i]
            resu[num] = i        