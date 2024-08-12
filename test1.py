def insert_operator(depth, total_cal, sum, sub, mul, div):
    global max_value
    global min_value

    if depth == N:
        max_value = max(total_cal, max_value)
        min_value = min(total_cal, min_value)
        return

    if sum > 0:
        insert_operator(depth + 1, total_cal + A[depth], sum - 1, sub, mul, div)
    if sub > 0:
        insert_operator(depth + 1, total_cal - A[depth], sum, sub - 1, mul, div)
    if mul > 0:
        insert_operator(depth + 1, total_cal * A[depth], sum, sub, mul - 1, div)
    if div > 0:
        # 나눗셈 처리: 음수일 경우와 아닐 경우를 구분해서 처리
        if total_cal < 0:
            insert_operator(depth + 1, -(-total_cal // A[depth]), sum, sub, mul, div - 1)
        else:
            insert_operator(depth + 1, total_cal // A[depth], sum, sub, mul, div - 1)


N = int(input())

A = list(map(int, input().split()))

operatorNum = list(map(int, input().split()))

# 최대값과 최소값 초기화
max_value = float('-inf')
min_value = float('inf')

insert_operator(1, A[0], operatorNum[0], operatorNum[1] ,operatorNum[2], operatorNum[3])

print(max_value)
print(min_value)
