T = int(input())

for i in range(T):
    R, S= input().split() #공백을 기준으로 R과 S를 나눔
    R = int(R) #문자를 숫자로 바꿈

    result = "" #R번 반복된 문자열을 새로 저장하기 위한 변수
    for j in range(len(S)):
        result += S[j] * R
    print(result)


