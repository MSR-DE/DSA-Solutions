class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       freq = {}

       for i in nums:
        freq[i] = freq.get(i,0)+1
    
    
       sortfreq = sorted(freq.items(), key= lambda i: i[1], reverse=True)

       result = [] ## top k numbers 

       for i in range(k):
        result.append(sortfreq[i][0])

       return result 
        