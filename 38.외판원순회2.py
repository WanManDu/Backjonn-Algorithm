def salesman(depth, current_city, visit, total_cost):
    global min_price

    # 모든 도시를 방문했으면, 시작 도시로 돌아오는 비용을 추가
    if depth == N:
        if moving_price[current_city][first_city] != 0:
            min_price = min(min_price, total_cost + moving_price[current_city][first_city])
        return

    # 현재 도시에서 방문할 수 있는 다른 도시를 탐색
    for next_city in range(N):
        if not visit[next_city] and moving_price[current_city][next_city] != 0:
            visit[next_city] = True
            salesman(depth + 1, next_city, visit, total_cost + moving_price[current_city][next_city])
            visit[next_city] = False

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
    salesman(1, start, visit, 0)

print(min_price)
