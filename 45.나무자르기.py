import sys

N ,M = map(int, input().split())

treeHeight = list(map(int, sys.stdin.readline().split()))

#나무 길이를 오름차순으로 정렬
treeHeight = sorted(treeHeight)

#시작점은 A[0]이 아니라 '나무 길이의 최솟값'인 0
#만약 A[0]을 start로 설정하면 문제가 발생
#A[1]부터 A[N - 1]까지의 나무를 잘라도 총 길이가 M에 도달하지 못할 수 있음
start = 0

#treeHeight를 정렬했으므로, treeHeight[N - 1]은 나무길이의 최댓값
end = treeHeight[N - 1]

#최종적인 절단기 높이 H를 저장할 변수
result = 0

#start가 end보다 커지면 반복문 종료(이분 탐색 종료조건)
while start <= end:
    #'절단기 높이'를 기준으로 이분탐색
    target = (start + end) // 2
    #자른 나무 길이들의 총 길이를 저장할 변수
    getTree = 0

    #자른 나무들의 길이의 합을 getTree에 저장
    for height in treeHeight:
        #target보다 짧은 나무는 자르지 않고 무시
        if height > target:
            getTree += height - target

    #만약 getTree의 값이 M보다 크거나 같으면, 
    #절단기의 높이를 올려서 자른 나무의 총 길이가 M보다 크지만 그전 결과보다 적게 자를 수 있는지 확인
    if getTree >= M:
        result = target
        start = target + 1

    #만약 getTree의 값이 M보다 작으면, 절단기의 높이를 낮춰야함
    if getTree < M:
        end = target - 1
        
#start의 값은 점점 올라가고, end의 값은 점점 낮아지니까, 
#getTree의 값이 M에 근사하면 start > end가 되므로 반복문 종료

print(result)
    


