N, M = map(int, input().split())

cardList = list(map(int, input().split()))

sum = 0
scoreList = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cardList[i] + cardList[j] + cardList[k] <= M:
                sum = cardList[i] + cardList[j] + cardList[k]
                scoreList.append(sum)


print(max(scoreList))
