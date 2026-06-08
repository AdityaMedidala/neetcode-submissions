class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for c in s:
            if c.isalnum():
                n+=c.lower()
        if n==n[::-1]:
            return True
        return False