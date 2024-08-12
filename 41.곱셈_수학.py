#시간초과

A, B, C = map(int, input().split())

num = A % C

for i in range(B):
    num *= A
    if num > C:
        num = num % C


print(num)
