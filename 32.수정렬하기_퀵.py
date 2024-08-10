from typing import MutableSequence

#런타임에러
def qsort(a, left, right):
    #a[left] ~ a[rigt]를 퀵 정렬
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)

def quick_sort(a):
    if len(a) > 0:
        qsort(a, 0, len(a) - 1)

num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

quick_sort(a)

for i in range(num):
    print(a[i])