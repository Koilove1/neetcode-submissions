class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        while left < right:
            while not s[right].isalnum() and left < right:
                right = right - 1
            while not s[left].isalnum() and left < right:
                left = left + 1
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1
        return True
    
         