class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        first_num = 0
        sec_num   = 1
        sum = 0
        
        for i in range(1, n, 1):
            sum = first_num + sec_num
            first_num = sec_num
            sec_num   = sum

        return sum
