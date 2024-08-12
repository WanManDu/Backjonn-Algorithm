# 오일러 법칙 사용
# 지수법칙 사용
# x를 y로 나눈 나머지가 m이면
# x^n을 y로 나눈 나머지는 m^n을 y로 나눈 나머지와 같다


def modular(A, B, C):
    #B 가 1 d이면, A를 C로 나눈 나머지 반환
    if B == 1:
        return A % C
    #B가 짝수이면
    #B를 2로 나눈 후 C로 나눈 나머지 반환
    elif B % 2 == 0:
        return (modular(A,B//2,C)**2)%C
    #B가 홀수이면
    #A^(B - 1)을 C로 나눈 값이 되니까
    #A를 한번 곱한뒤 다시 C로 나눈 값을 반환해야함
    else:
        return ((modular(A,B//2,C)**2)*A)%C

A, B, C = map(int, input().split())
print(modular(A, B, C))