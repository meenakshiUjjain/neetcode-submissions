class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2*n)
        for i in range(n):
            res[i] = res[n] = nums[i]
            n += 1
        return res
        