class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums is None:
            return []
        
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
                        

            