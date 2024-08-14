import math

#소수 구해주는 함수
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
    for m in range(3, square+1, 2):
        if n % m == 0:
            return 0
    return 1

def goldbach(n):
    #n 이하의 소수들을 모아둔 리스트
    primes = []
    for i in range(2, n):
        if prime(i) == 1:
            primes.append(i)

    #골츠바흐 숫자들의 조합을 저장하는 리스트
    #예)n이 10이라면 prime_set = [(3, 7), (5, 5)]
    prime_set = None

    #prime_set 안의 숫자들의 조합들 중 차이가 가장 작은 조합을 찾기 위한 것
    #예) (3,7)의 min_value = 4, (5,5)의 min_value = 0
    min_value = n
    for i in primes:

        #n - int(i) 가 소수인지 확인. 소수라면 pirme_set에 (int(i), n - int(i))가 저장됌
        #(int(i) - (n - int(i))) 가 min_value보다 작다면 min_value를 갱신해야함
        if prime(n - int(i)) and abs(2*int(i) - n) < min_value:
            prime_set = (int(i), n - int(i))
            min_value = abs(2*int(i) - n)
    
    return prime_set


test_case = int(input())
for i in range(test_case):
    n = int(input())
    p, q = goldbach(n)
    print(f"{p} {q}")