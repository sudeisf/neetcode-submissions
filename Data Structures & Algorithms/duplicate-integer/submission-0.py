class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        number_seen  = set()

        if not nums:
            return False

        for num in nums:
            if num in number_seen:
                return True
            number_seen.add(num)

        return False        