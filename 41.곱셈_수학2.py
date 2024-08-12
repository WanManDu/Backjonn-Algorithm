#시간초과

A, B, C = map(int, input().split())

num = A**B

for i in range(B):
    num = num % C
    if num < C:
        break


print(num)
