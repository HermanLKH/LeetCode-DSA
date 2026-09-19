class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        if len(s) == 0:
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return False

        return True