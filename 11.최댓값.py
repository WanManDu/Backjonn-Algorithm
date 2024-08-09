a = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9):
    a[i] = int(input())

max = max(a)
print(max)

for i in range(9):
    if a[i] == max:
        print(i + 1)