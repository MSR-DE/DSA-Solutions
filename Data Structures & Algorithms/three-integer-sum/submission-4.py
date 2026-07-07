class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        
        list1 = []

        for i in range(len(nums2)):
            if i > 0 and nums2[i] == nums2[i-1]:
                continue
            left = i + 1
            right = len(nums2) - 1

            while left < right:
                total = nums2[left]+nums2[right]+nums2[i]
                list2 = [nums2[left],nums2[right],nums2[i]]

                if total==0:
                    if list2 not in list1:
                        list1.append(list2)
                        left+=1
                        right-=1
                        while left < right and nums2[left] == nums2[left-1]:
                            left+=1
                
                elif total>0:
                    right-=1
                else:
                    left+=1
        return list1



            
        
        

        

        



