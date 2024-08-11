# current_city : 출발하는 도시
# visit : 도시를 방문했는지 여부를 확인
# total_cost : N개의 도시를 한바퀴 도는 비용을 합한 값
# min_price : total_cost중 최솟값을 저장


def salesman(depth, current_city, visit, total_cost, min_price):

    # 기저조건 : depth == N이되었을때, 현재 도시에서 처음 도시로 이동하는 비용이 0이 아니라면
    # 비용의 최솟값을 미리 저장된 값과 새로 탐색한 비용값을 비교하여 갱신함
    if depth == N:
        if moving_price[current_city][first_city] != 0:
            min_price = min(min_price, total_cost + moving_price[current_city][first_city])
        return min_price

    # 현재 도시에서 방문할 수 있는 다른 도시를 탐색
    for next_city in range(N):
        #백트래킹 조건 : 이미 방문한 도시가 아니고 이동 비용이 0이 아니면 재귀함수 호출
        if not visit[next_city] and moving_price[current_city][next_city] != 0:
            visit[next_city] = True
            min_price = salesman(depth + 1, next_city, visit, total_cost + moving_price[current_city][next_city], min_price)
            visit[next_city] = False
    return min_price

N = int(input())
moving_price = []

for i in range(N):
    city = list(map(int, input().split()))
    moving_price.append(city)

# 모든 요소가 False인 N x 1 행렬 선언
visit = [False] * N

# 비용의 최댓값을 초기 min_price로 설정
min_price = 4000000

# 모든 도시를 시작점으로 하여 탐색
for start in range(N):
    first_city = start
    visit[start] = True
    min_price = salesman(1, start, visit, 0, min_price)

print(min_price)
