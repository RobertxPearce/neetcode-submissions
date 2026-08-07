class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        
        for num in nums:
            count_map[num] += 1
        
        return heapq.nlargest(k, count_map.keys(), key=count_map.get)