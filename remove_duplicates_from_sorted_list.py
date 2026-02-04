t = int(input())

for _ in range(t):
    k = int(input())
    m = list(map(int,input().split()))
    
    j = list(set(m))
    print(sorted(j))
