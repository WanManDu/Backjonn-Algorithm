#city_lists : N개의 도시들에 방문하는 조합을 저장한다
# depth : 현재까지 방문한 도시의 개수
# used : 현재까지 방문한 도시의 index를 저장한다
#min_price : 현재까지 구한 최소 비용

def salesman(depth, used, min_price):

    if depth == N:
        totalSum = 0
        for i in range(0, N):
            totalSum += moving_price[i][next]
        min_price = min(min_price, totalSum)
        return min_price
    
    for i in range(N):
        for j in range(N):
            if moving_price[next][i] != 0 and i not in visited and value < min_value: 
            if i != j:
                if not used[i][j]:
                    used[i][j] = True
                    used[j][i] = True
                    min_price = salesman(price_lists + [moving_price[i][j]], depth + 1, used, min_price)
                    used[i][j] = False
                    used[j][i] = False
    return min_price

N = int(input())

moving_price = []

for i in range(N):
    city = list(map(int, input().split()))
    moving_price.append(city)

#모든 요소가 False인 N x N 행렬 선언
used = [False] * N

#4000000을 넣은 이유 : 각 도시간의 비용의 최댓값이 1,000,000이므로
#  4번 이동할 떄 최대 4,000,000의 비용이 든다.
min_price = salesman(0, used, 4000000)

print(min_price)