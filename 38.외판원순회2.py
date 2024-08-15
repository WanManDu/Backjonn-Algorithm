# current_city : 출발하는 도시
# visit : 도시를 방문했는지 여부를 확인하는 리스트
# total_cost : N개의 도시를 한바퀴 도는 비용을 합한 값
# min_price : 모든 경로 중 total_cost중 최솟값을 저장



def salesman(depth, current_city, visit, total_cost):
    global min_price

    # 기저조건 : depth == N이되었을때, 현재 도시에서 처음 도시로 이동하는 비용이 0이 아니라면
    # 비용의 최솟값을 미리 저장된 값과 새로 탐색한 비용값을 비교하여 갱신함
    if depth == N:
        if moving_price[current_city][first_city] != 0:
            min_price = min(min_price, total_cost + moving_price[current_city][first_city])
        return

    # 현재 도시에서 방문할 수 있는 다른 도시를 탐색
    for next_city in range(N):
        #moving_price의 값이 0인지 확인하고 지난적이 있는 도시인지 확인하는 것이 백트래킹 조건
        if not visit[next_city] and moving_price[current_city][next_city] != 0:
            visit[next_city] = True
            salesman(depth + 1, next_city, visit, total_cost + moving_price[current_city][next_city])
            visit[next_city] = False

N = int(input())
moving_price = []

for i in range(N):
    city = list(map(int, input().split()))
    moving_price.append(city)

# 방문 여부를 기록하는 모든 요소가 False인 N x 1 리스트 선언
visit = [False] * N

# 비용의 최댓값을 초기 min_price로 설정
min_price = 4000000

# 모든 도시를 시작점으로 하여 탐색
for start in range(N):
    first_city = start
    visit[start] = True #시작 도시를 방문한 것으로 표시
    salesman(1, start, visit, 0)
    #visit[start] = Falase 
    #'다음 시작점을 위해 초기화'하기위해 코드를 쳐도 되지만 재귀함수 호출이아니므로
    #적지 않아도 됌 
print(min_price)
