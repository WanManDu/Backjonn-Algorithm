def hanoi_function(n, start, end):
    if n == 1:
        print(start, end)
        return 
    
    hanoi_function(n-1, start, 6 - start - end)
    print(start,  end)
    hanoi_function(n-1, 6 - start - end, end)


n = int(input())

if n <= 20:
    print(2**n - 1)
    hanoi_function(n, 1, 3)

else:
    print(2**n - 1)