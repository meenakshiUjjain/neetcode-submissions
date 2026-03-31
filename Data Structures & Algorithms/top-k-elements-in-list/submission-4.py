class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = count.most_common(k)
        res = []
        for i in top_k:
            res.append(i[0])
        return res        