import math 

def prime(n):
    #2를 제외한 짝수는 다 소수
    if n == 2:
        return 1
    if n < 2:
        return 0
    if n > 2  and n % 2 == 0:
        return 0
    #n의 루트값
    square = int(math.sqrt(n)) + 1
    for m in range(3, square+1):
        if n % m == 0:
            return 0
    return 1
     
N = int(input())
numbers = list(map(int, input().split()))
prime_count = 0
for i in range(N):
    if prime(int(numbers[i])) == 1:
        prime_count += 1
print(prime_count)
