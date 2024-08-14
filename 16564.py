import sys
def level_management(start, end, charLevel, k):

    result = start

    while start <= end:
        lev = (start + end) // 2
        levelup = 0

        for l in charLevel:
            if l < lev:
                levelup += lev - l

        if levelup <= k:
            result = lev
            start = lev + 1
        else:
            end = lev - 1

    return result

N, K = map(int, input().split())
X = []

for i in range(N):
    x = int(input())
    X.append(x)

X.sort()

T = level_management(X[0], X[-1] + K, X, K)

print(T)
