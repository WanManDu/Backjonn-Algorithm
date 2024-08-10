#버블정렬
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

#bubble_sort실행

num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

bubble_sort(a)

for i in range(num):
    print(a[i])