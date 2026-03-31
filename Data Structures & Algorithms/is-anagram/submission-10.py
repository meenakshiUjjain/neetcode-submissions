class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        res = True
        
        if len(s) != len(t):
            res = False
            return res
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                res = False
        
        return res
        