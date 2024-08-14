#시간초과

import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

min = 1e10

result = ""

for i in range(N):
    for j in range(i + 1, N):
        sum = A[i] + A[j]
        if abs(sum) < min:
            min = abs(sum)
            result = A[i], A[j]

print(result[0], result[1])