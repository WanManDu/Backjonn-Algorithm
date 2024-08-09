A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = str(mul)

for i in range(10):
    print(mul.count(str(i)))