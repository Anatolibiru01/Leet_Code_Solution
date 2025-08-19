class Solution:
    def plusOne(self, digits):
        m = ""
        for num in digits:
            m += str(num)
        num = []
        for i in str(int(m) + 1):
            num.append(int(i))
        return num
