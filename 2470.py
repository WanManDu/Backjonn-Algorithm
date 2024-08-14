import sys

N = int(input())

L = list(map(int, sys.stdin.readline().split()))

L.sort()

start = 0
end = N - 1

mixed = abs(L[start] + L[end])
answer = [L[start], L[end]]

while start < end:

    if L[start] + L[end] < 0:
        if abs(L[start] + L[end]) < mixed:
            mixed = abs(L[start] + L[end])
            answer = [L[start], L[end]]
        start += 1
    
    elif L[start] + L[end] > 0:
        if abs(L[start] + L[end]) < mixed:
            mixed = abs(L[start] + L[end])
            answer = [L[start], L[end]]
        end -= 1

    elif L[start] + L[end] == 0:
        print(L[start], L[end])
        break

print(answer[0], answer[1])

