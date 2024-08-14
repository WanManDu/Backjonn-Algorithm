num = int(input())


for i in range(num):
    ans = list(input())
    total_score = 0
    plus_score = 0
    for i in ans:
        if i == 'O':
            plus_score += 1
            total_score += plus_score
        elif i =='X':
            #plus_score 초기화
            plus_score = 0
    print(total_score)