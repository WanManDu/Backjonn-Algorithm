num = int(input())
ans = list(input())

for i in range(num):
  
    score = 0
    plus_score = 0
    for i in ans:
        if i == 'O':
            plus_score += 1
            score = score+plus_score
        elif i =='X':
            plus_score = 0
    print(score)