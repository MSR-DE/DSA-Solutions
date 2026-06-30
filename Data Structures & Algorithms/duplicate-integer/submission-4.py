class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seesn = set()
        for i in nums:
            if i in seesn:
                return True
            else:
                seesn.add(i)
        return False