heightList = []

for i in range(9):
    heightList.append(int(input()))

allHeight = 0
for i in range(9):
    allHeight += heightList[i]

#합이 100이 되기 위해 제거해야 할 두 난쟁이의 키 합 계산
key = allHeight - 100

#가짜들을 찾기위해 변수 생성
fake1 = 0
fake2 = 0

#합이 key인 두 난쟁이 찾기
for i in heightList:
    for j in heightList:
        if i == j:
            continue
        if key == i + j:
            fake1 = i
            fake2 = j
            break


#두 난쟁이의 키를 heightList에서 제거하기
heightList.remove(fake1)
heightList.remove(fake2)

heightList.sort()
#오름차순으로 일곱난장이 키 출력
for i in heightList:
    print(i)