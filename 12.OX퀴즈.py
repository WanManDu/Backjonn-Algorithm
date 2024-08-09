#n은 문제 개수, quiz는 OX문제, score은 총 점수, count는 해당 'O'의 점수
#두번째 for문의 if 문에서 'X'를 검증하는게 빠를까 'O'를 검증하는게 빠를까?
#'X'를 먼저 판별하게 되면 요소가 'O'인지 확인해야 한다. 
#하지만 'O'를 먼저 판별하면 'O'이외의 모든것 으로 처리가 되므로 'X'를 판별하지 않아도 된다.

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



