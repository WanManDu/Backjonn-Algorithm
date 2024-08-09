import bisect

x, y = map(int, input().split())

n = int(input())
list_x = []
list_y = []

list_x.append(0)
list_y.append(0)

for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        for i in range(len(list_y)):
            if list_y[i] < b:
                bisect.insort(b, i + 1)

    if a == 1:
        for i in range(len(list_x)):
            if list_x[i] < b:
                bisect.insort(b, i + 1)

list_x.append(x)
list_y.append(y)

max_x = 0
max_y = 0

for i in range(1, len(list_x)):
    if list_x[i] - list_x[i-1] > max_x:
        max_x = list_x[i] - list_x[i-1]
for i in range(1, len(list_y)):
    if list_y[i] - list_y[i-1] > max_y:
        max_y = list_y[i] - list_y[i-1]

print(max_x * max_y)