def fsort(a, max_val):
    # 도수 정렬
    n = len(a)
    f = [0] * (max_val + 1)  # 도수 배열
    b = [0] * n  # 정렬된 배열

    # 도수 계산
    for i in range(n):
        f[a[i]] += 1

    # 누적 도수 계산
    for i in range(1, max_val + 1):
        f[i] += f[i - 1]

    # 배열 b에 정렬하기
    for i in range(n - 1, -1, -1):
        b[f[a[i]] - 1] = a[i]
        f[a[i]] -= 1

    # 원래 배열 a에 정렬된 값 복사
    for i in range(n):
        a[i] = b[i]

def counting_sort(a):
    # 도수 정렬
    fsort(a, max(a))

# 입력
num = int(input())
a = []

for i in range(num):
    m = int(input())
    a.append(m)

# 정렬
counting_sort(a)

# 출력
for i in range(num):
    print(a[i])
