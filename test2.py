import sys

N, B = map(int, input().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

C = 1000

#행렬A와 행렬 B의 곱을 계산해 주는 함수
def matrix_multiply(A, B):
    #결과를 저장할 행렬을 0으로 초기화(N * N 크기)
    martirx_mul = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # A, B, C 행렬이 N * N 행렬이고
            # C행렬이 A행렬과 B행렬의 곱일 때,
            # C[3][5] = A[3][1]B[1][5] + A[3][2]B[2][5] + ... + A[3][N]B[N][5]
            #k가 1부터 N까지 변한다고 볼 수 있음
            for k in range(N):
                martirx_mul[i][j] += A[i][k] * B[k][j]
                martirx_mul[i][j] = martirx_mul[i][j] % 1000
    return martirx_mul
    

def solution(A, B):
    # B가 1일 때, A 의 원소를 1000로 나눈 나머지를 반환
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % C
        return A

    #B가 짝수일 때, 행렬 A를 B//2로 제곱한 결과를 두번 곱함(반으로 나눈 행렬의 제곱)
    if B % 2 == 0:
        half = solution(A, B // 2)
        return matrix_multiply(half, half)

    #B가 홀수일 때, B//2 제곱한 결과를 두번 곱하고, 추가로 행렬 A를 한번 더 곱해줌
    if B % 2 == 1:
        half = solution(A, B // 2)
        return matrix_multiply(matrix_multiply(half, half), A)
    
result = solution(A, B)

#결과 행렬의 각 행을 출력
for row in result:
    print(' '.join(map(str, row)))