class Solution:
    def isPalindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

        # inaproprate answer
        # s = str(x)
        # r = []
        # for i in range(len(s)):
        #     if s[i] == s[-(i+1)]:
        #         r.append("t")
        #     else:
        #         r.append("f")
        # if "f" in r:
        #     return False
        # else:
        #     return True
