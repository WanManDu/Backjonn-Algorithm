def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

#insertion_sort 호출

num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

insertion_sort(a)

for i in range(num):
    print(a[i])