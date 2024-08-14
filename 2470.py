import sys

# 용액의 개수 입력
N = int(input())

# 용액의 리스트 입력
L = list(map(int, sys.stdin.readline().split()))

# 용액 리스트를 오름차순 정렬
L.sort()

# 초기값 설정
start = 0
end = N - 1

min_mixed = abs(L[start] + L[end])
answer = [L[start], L[end]]

# start가 end보다 작을 때까지 반복
while start < end:
    current_sum = L[start] + L[end]

    # 현재의 합이 이전 최솟값보다 작은 경우
    if abs(current_sum) < min_mixed:
        min_mixed = abs(current_sum)
        answer = [L[start], L[end]]

    # 합이 0보다 작으면 start 포인터를 오른쪽으로 이동
    if current_sum < 0:
        start += 1

    # 합이 0보다 크면 end 포인터를 왼쪽으로 이동
    elif current_sum > 0:
        end -= 1

    # 합이 0이면 종료 (최적의 답이므로)
    else:
        break

print(answer[0], answer[1])
