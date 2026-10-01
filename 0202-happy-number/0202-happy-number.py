class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = {}
        
        while not seen.get(n):
            seen[n] = 1
            str_n = str(n)
            n = 0

            for i, c in enumerate(str_n):
                int_n = int(c)

                n += int_n ** 2
            
            if n == 1:
                return True
                
        return False
