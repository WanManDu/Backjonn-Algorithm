n, x= map(int,input().split())


while True:
    a = list(map(int, input("두 번째 줄 입력 (a 리스트): ").split()))
    if len(a) == n:
        break
    else:
        print(f"Error: a 리스트의 길이가 {n}과 다릅니다. 다시 입력하세요.")

for i in range(n):
    if x>a[i]:
        print(a[i],end=' ')
