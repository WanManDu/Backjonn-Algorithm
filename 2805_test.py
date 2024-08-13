import sys

N ,M = map(int, input().split())

treeHeight = list(map(int, sys.stdin.readline().split()))

treeHeight = sorted(treeHeight)

getTree = 0
min = 1e10

for height in treeHeight:
    start = treeHeight[0]
    end = treeHeight[N - 1]

    while start <= end:
        target = (start + end) // 2

        for i in range(target, N):
            getTree += treeHeight[i] - height

        if getTree == M:
            print(height)
            break

        if getTree > M:
            start = target + 1

        if getTree < M:
            end = target - 1

        min = min(min, abs(height - treeHeight[target]))

print(M + min)
    