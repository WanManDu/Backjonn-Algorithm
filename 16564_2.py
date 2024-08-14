import sys

def level_management(start, end, charLevel, k):
    
    if start > end:
        return end
    
    lev = (start + end) // 2
    levelup = 0

    #현재의 레벨과 lev를 비교하였을 때, 현재의 레벨이 lev보다 작다면
    #lev까지 lev - (현재레벨) 만큼 레벨을 올려야함
    #올린 레벨은 levelup에 저장하고 levelup의 값을 기준으로 반복여부를 정함
    for each_level in charLevel:
        if each_level < lev:
            levelup += lev - each_level

    if levelup <= k:
        return level_management(lev + 1, end, charLevel, k)
    else:
        return level_management(start, lev - 1, charLevel, k)



N, K = map(int, input().split())

X = []

for i in range(N):
    x = int(input())
    X.append(x)

X.sort()

T = level_management(X[0], X[-1] + K, X, K)

print(T)



