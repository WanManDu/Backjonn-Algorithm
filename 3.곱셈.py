#A, B = map(int, input().split())

#C = B % 10
#D = B % 100
#E = B % 1000

#print(A * C)
#print(A * (D - C) // 10)
#print(A * (E - D) // 100)
#print(A * B)
#위 코드는 런타임 에러를 발생시킴 왜? C, D, E가 값이 같을 경우가 생길 수 있음
#A, B = map(int, input().split())

#C = B % 10  # 일의 자리 숫자
#D = (B % 100) // 10  # 십의 자리 숫자
#E = (B % 1000) // 100  # 백의 자리 숫자

#print(A * (B % 10))  # A * 일의 자리
#print(A * (B % 100) // 10)  # A * 십의 자리
#print(A * (B % 1000) // 100)  # A * 백의 자리
#print(A * B)  # A * B 전체
#위 코드도 런타임 에러가 발생

a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))
