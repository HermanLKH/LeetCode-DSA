class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        first_num = 0
        sec_num   = 1
        
        for _ in range(1, n):
            first_num, sec_num = sec_num, first_num + sec_num

        return sec_num
