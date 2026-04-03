class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        k = count.most_common(1)[0][0]

        return k