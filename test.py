import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree_list = list(map(int, input().split()))
start = 0
end = max(tree_list)
answer = 0
while start <= end:
    half = (start + end) // 2
    total = 0
    for tree in tree_list:
        if tree - half > 0:
            total += (tree - half)
    if total == M:
        answer = half
        break
    if total > M:
        start = half + 1
        answer = max(answer, half)
    else:
        end = half - 1
print(answer)
        
