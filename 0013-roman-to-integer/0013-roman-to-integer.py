class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,   'V': 5, 
            'X': 10,  'L': 50, 
            'C': 100, 'D': 500, 
            'M': 1000
        }
        num  = 0

        for i, rc in enumerate(s):
            curr = roman_numerals[rc]

            if i + 1 < len(s) and curr < roman_numerals[s[i + 1]]:
                num -= curr
            else:
                num += curr

        return num