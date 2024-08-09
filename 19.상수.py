A1, B1 = input().split()

A2 = A1[::-1]
B2 = B1[::-1]

A3 = int(A2)
B3 = int(B2)

if A3 > B3: 
    print(A3)
if A3 < B3: 
    print(B3)