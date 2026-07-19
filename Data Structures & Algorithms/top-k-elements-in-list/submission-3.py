class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        for num in nums:
            frequent[num]+=1  
        sorted_items = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for num, freq in sorted_items[:k]:
            res.append(num)

        return res
