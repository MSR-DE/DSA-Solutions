class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' target is bigger or smaller than the result 
            would define if left moves or right'''
        l=0
        r=len(numbers)-1

        while l<r:
            while l<r and numbers[l]+numbers[r]<target:
                l+=1
            while l<r and numbers[l]+numbers[r]>target:
                r-=1
            while l<r and numbers[l]+numbers[r]==target:
                return[l+1, r+1]


        