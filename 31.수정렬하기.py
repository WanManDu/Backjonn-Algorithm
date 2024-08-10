num = int(input())
list = []

for i in range(num):
    m = int(input())
    list.append(m)

list.sort()

for i in range(num):
    print(list[i])
