a = []

n = int(input())

score = 0
count = 1

for i in range(n):
    # 리스트에 값을 추가할 때는 append() 사용
    a.append(input())


for i in range(n):
    a[i] = input()
    if a[i] == 'O':
        for j in range(i):
            if a[j] == 'O':
                score += count
                count += 1
            else:
                count = 1



print(score)
