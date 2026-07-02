class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for  index, i in enumerate(nums):
            diff = target - i

            if diff in seen:
                return[seen[diff], index]

            seen[i]=index
        



