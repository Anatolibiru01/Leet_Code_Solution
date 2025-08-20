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
    # c++ version
# class Solution {
# public:
#     bool isPalindrome(int x) {
#     {
#         string s;
#         string reverse_s = "";
#         s = to_string(x);
#         for (int i = (s.length() - 1); i >= 0; i--)
#         {
#             reverse_s += s[i];
#         }
#         return s == reverse_s;
#     }
#     }
# };
