

N, C = map(int,input().split())

A = []

for i in range(N):
    A.append(int(input()))


A.sort()

#'집들간의 거리'를 기준으로 이분탐색.
start = 1
end = A[N - 1] - A[0]

result = 0

while start <= end:
    current = A[0]
    count = 1
    mid = (start + end) // 2
    for i in range(1, N):
        if A[i] - current >= mid:
            count += 1
            current = A[i]
    if count >= C:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)