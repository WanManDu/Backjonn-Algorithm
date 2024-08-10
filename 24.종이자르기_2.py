x, y = map(int, input().split())

n = int(input())
list_x = [0, x]
list_y = [0, y]

for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        list_y.append(b)
    if a == 1:
        list_x.append(b)


if len(list_x) > 1:
    list_x.sort()
if len(list_y) > 1:
    list_y.sort()

max_x = 0
max_y = 0

for i in range(1, len(list_x)):
    max_x = max(max_x, list_x[i] - list_x[i-1])


for i in range(1, len(list_y)):
    max_y = max(max_y, list_y[i] - list_y[i-1])


print(max_x * max_y)