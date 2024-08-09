def hansu(n):
    if n <= 100:
        return n - 1
    else:
        count = 99
        for x in range(100, n+1):
            num_str = str(n)
            d = int(num_str[1]) - int(num_str[0])
            x = True
            for m in range(1, len(num_str)):
                if int(num_str[m]) - int(num_str[m-1]) != d:
                    x = False
                    break
        
            if x:
                count += 1
    return count
    
print(hansu(88))
print(hansu(105))