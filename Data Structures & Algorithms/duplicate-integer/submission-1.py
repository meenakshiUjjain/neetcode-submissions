class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        result = False

        if len(nums) == 0:
            result = False
        else:
            count = Counter(nums)
            max_value = max(count.values())
            if max_value > 1:
                result = True 

        return result
        