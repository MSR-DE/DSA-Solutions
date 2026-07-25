class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        add1 = []
        add2 = []

        if len(s)==len(t):
            for i in s:
                add1.append(i)
            for i in t:
                add2.append(i)

            if sorted(add1)== sorted(add2):
                return True
            else: 
                return False

        else:
            return False
        