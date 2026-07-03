class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       count = {}

       for i in nums:
        count[i] = count.get(i,0)+1
    

       ## creating buckets
       freq = [[]for i in range(len(nums)+1)]

       ## numbers into their buckets
       for num,c in count.items():
        freq[c].append(num)

       result = []

       for i in range(len(freq)- 1,0,-1): 
        for num in freq[i]:
            result.append(num)

            if len(result) == k:
                return result


     
        