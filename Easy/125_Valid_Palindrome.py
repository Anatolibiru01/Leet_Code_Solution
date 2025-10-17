class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        g = ""
        for i in range(len(s)):
            if s[i] not in string.punctuation and s[i] not in string.whitespace:
                g += s[i].lower()

        return g == g[::-1]
