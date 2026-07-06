class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index, i in enumerate(numbers):

            for index2, n in enumerate(numbers):

                if i + n == target and index < index2:
                    return [index+1, index2+1] 

                
        