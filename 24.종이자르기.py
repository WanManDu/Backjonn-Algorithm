x, y = map(int, input().split())

n = int(input())
list_x = [0, x]  # 초기 x 범위 (0과 x)
list_y = [0, y]  # 초기 y 범위 (0과 y)

# 자르는 위치를 리스트에 추가
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        list_y.append(b)  # y 방향으로 자름
    elif a == 1:
        list_x.append(b)  # x 방향으로 자름

# 리스트가 비어있거나 크기가 작아도 동작할 수 있도록 안전하게 정렬
if len(list_x) > 1:
    list_x.sort()
if len(list_y) > 1:
    list_y.sort()

# 가장 큰 x 간격과 y 간격 찾기
max_x = 0
max_y = 0

# x 간격 계산
for i in range(1, len(list_x)):
    max_x = max(max_x, list_x[i] - list_x[i-1])

# y 간격 계산
for i in range(1, len(list_y)):
    max_y = max(max_y, list_y[i] - list_y[i-1])

# 가장 큰 직사각형의 넓이 출력
print(max_x * max_y)
