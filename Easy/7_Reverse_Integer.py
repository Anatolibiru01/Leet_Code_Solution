class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        rev_int = int(str(abs(x))[::-1]) * sign
        if rev_int < -2**31 or rev_int > 2**31 - 1:
            return 0
        return rev_int
