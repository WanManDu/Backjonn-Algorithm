n = int(input())

count = 99

if n < 100:
    print(n)

else:
    for x in range(100, n+1):
        num_str = str(x)
        d = int(num_str[1]) - int(num_str[0])
        verify = True

        for m in range(1, len(num_str)):
            if int(num_str[m]) - int(num_str[m - 1]) != d:
                verify = False
                break

        if verify:
            count += 1
    print(count)