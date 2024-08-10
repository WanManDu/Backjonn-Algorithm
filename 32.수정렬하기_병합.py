def heap_sort(a):
    #힙 정렬
    def down_heap(a, left, right):
        #a[left] ~ a[right]를 힙으로 만들기
        temp = a[left]

        #a[i]의 부모요소는 a[(i - 1) // 2], 왼쪽 자식노드 a[i * 2 + 1], 오른쪽 자식노드 a[i * 2 + 2]
        parent = left
        while parent < (right + 1) //2:
            cl = parent * 2 + 1 #왼쪽 요소
            cr = cl + 1         #오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl #큰값을 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1): #배열을 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1): #배열에서 최댓값인 루트 노드를 뺀 뒤 다시 배열을 힙으로 만들기
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

heap_sort(a)

for i in range(num):
    print(a[i])