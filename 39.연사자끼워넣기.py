
def insert_operator(depth, total_cal, sum, sub, mul, div):
    global min_value, max_value

    if depth == N:
        max_value = max(max_value, total_cal)
        min_value = min(min_value, total_cal)
        return
    
    if sum > 0:
        insert_operator(depth + 1, total_cal + A[depth], sum - 1, sub, mul, div)
    if sub > 0:
        insert_operator(depth + 1, total_cal - A[depth], sum, sub - 1, mul, div)    
    if mul > 0:
        insert_operator(depth + 1, total_cal * A[depth], sum, sub, mul - 1, div)
    if div > 0:
        insert_operator(depth + 1, int(total_cal / A[depth]), sum, sub, mul, div - 1)    


N = int(input())

A = list(map(int, input().split()))

operatorNum = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')

insert_operator(1, A[0], operatorNum[0], operatorNum[1], operatorNum[2], operatorNum[3])

print(max_value)
print(min_value)