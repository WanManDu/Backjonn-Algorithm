#n : 행과 열의 개수
#i : 각 행의 번호
#count : 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

def N_Queens(n, i, count):
    #j열의 알맞은 위치에 퀸을 배치
    for j in range(n):
        #J열, 왼쪽대각선, 오른쪽 대각선에 퀸이 없는지 확인
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i - j + (n - 1)]:
            pos[i] = j
            #마지막 행에 퀸을 배치한 뒤에 count를 1 올리고 종료
            if i == n - 1:
                count += 1
            else:
                #퀸의 위치를 기록하여 다음 퀸 배치를 위한 상태 업데이터
                flag_a[j] = True
                flag_b[i+j] = True
                flag_c[i-j+(n-1)] = True
                #다음 행으로 이동하여 퀸 배치 시도
                count = N_Queens(n, i + 1, count) 
                flag_a[j] = False
                flag_b[i+j] = False
                flag_c[i-j+(n-1)] = False
    return count

n = int(input())

pos = [0] * n # 각 행의 퀸의 위치
flag_a = [False] * n # 각 열에 퀸이 있는지 확인
flag_b = [False] * (2 * n - 1) #오른쪽 대각선에 퀸이 있는지 확인
flag_c = [False] * (2 * n - 1) #왼쪽 대각선에 퀸이 있는지 확인

#i = 0 부터 시작, 초기 count = 0,
print(N_Queens(n, 0, 0))