def hanoi_count(n):
    if n == 1:
        return 1
    return 2 * hanoi_count(n - 1) + 1

def hanoi_function(n, start, end):
    if n == 1:
        print(start, end)
        return 
    
    hanoi_function(n-1, start, 6 - start - end)
    print(start,  end)
    hanoi_function(n-1, 6 - start - end, end)


n = int(input())

if n <= 20:
    print(hanoi_count(n))
    hanoi_function(n, 1, 3)

else:
    print(hanoi_count(n))