import math

def prime(n):
    if n == 1:
        return 0
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

def goldbach(n):
    primes = []
    for i in range(2, n):
        if prime(i) == 1:
            primes.append(i)

    prime_set = None
    min_value = n
    for i in primes:
        if prime(n - int(i)) and abs(2*int(i) - n) < min_value:
            prime_set = (int(i), n - int(i))
            min_value = abs(2*int(i) - n)
    return prime_set


test_case = int(input())
for i in range(test_case):
    n = int(input())
    p, q = goldbach(n)
    print(f"{p} {q}")