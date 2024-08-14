import sys

#용액의 개수 입력
N = int(input())

#용액의 리스트 입력
L = list(map(int, sys.stdin.readline().split()))

#용액의 리스트를 오름차순 정렬
L.sort()

#용액 리스트의 첫 값과 끝 값을 합치는 것부터 시작
start = 0
end = N - 1

min_mixed = abs(L[start] + L[end])
answer = [L[start], L[end]]

#start가 end보다 크거나 같아지면 반복문 종료
while start < end:

    #만약 
    if L[start] + L[end] < 0:
        if abs(L[start] + L[end]) < min_mixed:
            min_mixed = abs(L[start] + L[end])
            answer = [L[start], L[end]]
        start += 1
    
    if L[start] + L[end] > 0:
        if abs(L[start] + L[end]) < min_mixed:
            min_mixed = abs(L[start] + L[end])
            answer = [L[start], L[end]]
        end -= 1

    if L[start] + L[end] == 0:
        print(L[start], L[end])
        break

print(answer[0], answer[1])