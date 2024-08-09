T = int(input())

for i in range(T):
    R, S= input().split() #공백을 기준으로 R과 S를 나눔
    R = int(R) #문자를 숫자로 바꿈

    result = "" #[]를 사용하면 반복되는 문자들이 각각 저장되는 문제가 생김
    for j in range(len(S)):
        result += S[j] * R
    print(result)


