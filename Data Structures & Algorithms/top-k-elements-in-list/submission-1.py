from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_numbers = defaultdict(int)

        for num in nums:
                frequent_numbers[num] +=1
        
        return heapq.nlargest(k,frequent_numbers, key=frequent_numbers.get)