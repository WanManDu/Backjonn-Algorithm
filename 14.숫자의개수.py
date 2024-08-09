A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = str(mul)
mul_num = [0]*10
for i in mul:
    mul_num[int(i)] += 1
for i in mul_num:
    print(i)