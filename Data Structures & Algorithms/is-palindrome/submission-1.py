class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = list(s.lower())

        newforward = []

        for i in forward:
            
            if i.isalnum():
                newforward.append(i)
            
        backward = newforward[::-1]

        return backward == newforward





        


            

