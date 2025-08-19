class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # this code is not working for s = "a"
        # for i in range((len(s)-1), 1, -1):
        #     if s[i] == " ":
        #         continue
        #     else:
        #         m = ""
        #         for j in range(i, 1, -1):
        #             if s[j] != " ":
        #                 m += s[j]
        #             else:
        #                 break
        #         break
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        num = 0
        while i >= 0 and s[i] != " ":
            num += 1
            i -= 1
        return num
