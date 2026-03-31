class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res= []
        count = Counter(nums)
        top_k = count.most_common(k)
        for n in top_k:
            res.append(n[0])
        return res
        