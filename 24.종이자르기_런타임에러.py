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


list_x.sort()
list_y.sort()

max_x = 0
max_y = 0

for i in range(1, len(list_x)):
    if list_x[i] - list_x[i-1] > max_x:
        max_x = list_x[i] - list_x[i-1]
for i in range(1, len(list_y)):
    if list_y[i] - list_y[i-1] > max_y:
        max_y = list_y[i] - list_y[i-1]

print(max_x * max_y)