#단순 선택 정렬

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


#selection_sort 호출

num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

selection_sort(a)

for i in range(num):
    print(a[i])

