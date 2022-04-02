class Solution:
    def romanToInt(self, s: str) -> int:
        table1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        table2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        c = 0
        val = 0
        while c < len(s):
            
            if s[c:c+2] in table2:
                val += table2[s[c:c+2]]
                c += 2
                
            elif s[c] in table1:
                val += table1[s[c]]
                c += 1
                
        return val
        