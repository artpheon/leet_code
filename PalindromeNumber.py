class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]