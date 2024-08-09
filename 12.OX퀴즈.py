n = int(input())

for i in range(n):
    quiz = list(input())
    score = 0
    count = 0
    for j in quiz:
        if j == 'O':
            count += 1
            score = score + count
        else:
            count = 0
    print(score)



