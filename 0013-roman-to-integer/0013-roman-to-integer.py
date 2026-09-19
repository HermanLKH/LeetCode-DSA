class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,   'V': 5, 
            'X': 10,  'L': 50, 
            'C': 100, 'D': 500, 
            'M': 1000
        }
        num  = 0
        val  = 0
        fast = 1

        for slow in range(len(s)):
            if fast - slow == 1:
                curr = roman_to_int[s[slow]]
                next = roman_to_int[s[fast]] if fast < len(s) else None
                
                if next and curr < next:
                    num += curr * -1 + next
                    fast += 2
                else:
                    num += curr
                    fast += 1

        return num