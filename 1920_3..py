#시간초과

import sys

def binary_search(numList, searchList, checkList):


    for i in range(M):
        pl = 0
        pr = len(numList) -1
        key = searchList[i]
        while pl <= pr:
            pc = (pl + pr) // 2
            if numList[pc] == key:
                checkList[i] = 1
                break
            if numList[pc] < key:
                pl = pc + 1
            if pr == pc - 1:
                pr = pc - 1
    
    return checkList
        




N = int(input())

A = list(map(int,input().split()))

M = int(input())

B = list(map(int, input().split()))

C = [0] * M


binary_search(A, B, C)


for i in C:
    print(i)