def absSum(number_lists, depth, used, maxSum):
    #기저조건 :  depth가 N에 도달하면
    # number_lists에 있는 연속되는 요소들의 차의 절댓값들의 합을 totalSum에 저장
    if depth == N:
        totalSum = 0
        for i in range(1, N):
            totalSum += abs(number_lists[i] - number_lists[i - 1])
        #현재 계산된 totalSum과 이전의 maxSum 중 더 큰값을 반환
        maxSum = max(maxSum, totalSum)
        return maxSum

    for i in range(N):
        if not used[i]:
            used[i] = True
            #maxSum에 absSum을 넣는 이유는 갱신된 maxSum을 반영하기 위해서이다.
            maxSum = absSum(number_lists + [A[i]], depth + 1, used, maxSum)
            used[i] = False
    #최종 반환값. 재귀호출에서 반환된 maxSum을 게속 갱신하며 최종적으로 최대값을 반환함
    return maxSum

N = int(input())

A = list(map(int, input().split()))

used = [False] * N

#최종적으로 계산된 maxSum이 max_result에 저장됨
max_result = absSum([], 0, used, 0)

print(max_result)