class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
        # for i in range(len(s)):
        #     if s[i] not in s[0:i]+s[i+1:]:
        #         return i
        # return -1
            
        