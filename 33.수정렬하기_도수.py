#도수정렬

#숫자가 1000만개가 주어질 수 있기 때문에 배열에 저장하면 메모리 초과가 발생할 수 있음

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

dosuList = [0] * 10001

#입력하는 숫자의 개수를 dosuList에 저장
for i in range(n):
    dosuList[int(input())] += 1

for i in range(1, 10001):
    for j in range(dosuList[i]):
        #str에 개행이 안들어 가기 때문에 '\n'을 넣어줌
        print(str(i) + '\n')