# t = int(input())

# for _ in range(t):
#     a = input()
#     b = input()
#     ab = int(a, 2) + int(b, 2)
#     print(f"\"{format(ab, "b")}\"")
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k = int(a,2) + int(b,2)
        return format(k, "b")