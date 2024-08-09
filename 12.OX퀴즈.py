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
            count = 0 #X가 나타나면 count가 0이 되므로 X다음의 O는 그 앞의 O는 의식하지 않아도됌
    print(score)



