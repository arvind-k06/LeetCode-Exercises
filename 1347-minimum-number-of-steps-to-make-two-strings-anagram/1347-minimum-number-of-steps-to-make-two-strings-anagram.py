class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for i in t:
            s = s.replace(i,"",1)
        print(s)
        return len(s)
        