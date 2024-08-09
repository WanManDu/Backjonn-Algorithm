#재미로 푸는 알고리즘
#min 함수를 사용하지 않고 최솟값을 찾을 수 있을까?

a = [9, 5, 3, 8, 1, 7,]

min = a[0]

for i in range(1, len(a)):
    if a[i] < min:
        min = a[i]


print(min)