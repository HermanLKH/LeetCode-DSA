class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,   'V': 5, 
            'X': 10,  'L': 50, 
            'C': 100, 'D': 500, 
            'M': 1000
        }
        num  = 0
        fast = 1

        for slow in range(len(s)):
            if fast - slow == 1:
                curr_val = roman_to_int[s[slow]]
                next_val = roman_to_int[s[fast]] if fast < len(s) else None
                
                if next_val and curr_val < next_val:
                    num += curr_val * -1 + next_val
                    fast += 2
                else:
                    num += curr_val
                    fast += 1

        return num