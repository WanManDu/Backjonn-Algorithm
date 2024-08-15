import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

A = sorted(A)

M = int(input())

B = list(map(int, sys.stdin.readline().split()))

for key in B:
    pl = 0
    pr = N - 1

    while pl <= pr:
        pc = (pl + pr) // 2

        #key 값이 A[pc]값과 같으면 1 출력
        if key == A[pc]:
            print(1)
            break
        #A를 오름차순으로 정렬했기 때문에 A[pc]의 오른쪽에는 A[pc]보다 큰 값만 있음
        if key > A[pc]:
            pl = pc + 1
        #A를 오름차순으로 정렬했기 때문에 A[pc]의 왼쪽에는 A[pc]보다 작은 값만 있음
        if key < A[pc]:
            pr = pc - 1

    else:
        print(0)