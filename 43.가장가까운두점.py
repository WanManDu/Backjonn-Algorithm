import sys
import math

#두 점 사이의 거리를 계산
def calculate_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closest_pair(points, left, right):

    #한 구역 안에 점이 3개 이하일때는 완전탐색으로 점들의 거리 구함
    if right - left <= 3:
        min_dist = float('inf')
        for i in range(left, right):
            for j in range(i + 1, right):
                dist = calculate_distance(points[i], points[j])
                min_dist = min(min_dist, dist)
        return min_dist

    #중간을 기준으로 좌, 우로 나눔
    mid = (left + right) // 2
    mid_x = points[mid][0]

    #왼쪽, 오른쪽 구역에서 최소 거리를 구하고, 경계선 근처에 있는 점들간의 거리 비교하기
    dist_left = closest_pair(points, left, mid)
    dist_right = closest_pair(points, mid, right)
    min_dist = min(dist_left, dist_right)

    #경계선과 min_dist 거리보다 가까이 있는 점들끼리만의 거리를 다시 비교
    in_strip = []
    for i in range(left, right):
        if abs(points[i][0] - mid_x) ** 2 < min_dist:
            in_strip.append(points[i])

    #y값을 기준으로 정렬(이렇게 하면 y값 차가 적은 점들만 비교하면 됨)
    in_strip.sort(key=lambda point: point[1])

    #남아있는 점들의 y값을 비교하고, min_dist보다 차이가 큰 점들끼리의 거리는 제외
    for i in range(len(in_strip)):
        for j in range(i + 1, len(in_strip)):
            #y축 거리 차이가 min_dist보다 크면 더 이상 비교할 필요가 없음
            if (in_strip[j][1] - in_strip[i][1]) ** 2 >= min_dist:
                break
            dist = calculate_distance(in_strip[i], in_strip[j])
            min_dist = min(min_dist, dist)

    return min_dist

N = int(input())

points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#points의 점들을 x값을 기준으로 정렬
points.sort()

#분할 정복을 통해 최단 거리의 제곱을 계산
min_distance_squared = closest_pair(points, 0, N)

#최단 거리의 제곱값 출력
print(min_distance_squared)



        