C = int(input())


for i in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    scores =data[1:]

    ave = sum(scores) / N

    count = 0
    for score in scores:
        if score > ave:
            count += 1
        
    per = (count / N) * 100
    print(f"{per:.3f}%")


