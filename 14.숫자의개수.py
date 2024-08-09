A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = str(mul)
mul_temp = [0]*10
for i in mul:
    mul_temp[int(i)] += 1
for i in mul_temp:
    print(i)