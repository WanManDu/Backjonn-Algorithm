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
     

def goldbach(n):
    list = [2, ]
    primes = []
    prime_sum = []
    for i in range(1, n):
        if prime(i) == 1:
            list.append(i)
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == n:
                primes.append([list[i], list[j]])
                prime_sum.append(abs(list[i] - list[j]))
    
    return prime_sum, primes

test_case = int(input())

for i in range(test_case):
    n = int(input())
    print(goldbach(n))