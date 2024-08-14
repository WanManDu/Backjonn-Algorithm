import sys

M, N, L = map(int, sys.stdin.readline().split())

Hunter = list(map(int, sys.stdin.readline().split()))

Animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for i in Hunter:
    print(i)

for i in Animal:
    print(i)
