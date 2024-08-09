n = int(input())
test_scores = []
for i in range(n):
    test_result = input()
    successive = 0
    test_score = 0 #위에 test_score = []가 있는 데 왜 초기화 한거지?
    for i in test_result:
        if i =='X':
            successive = 0
            continue
        else:
            successive += 1
            test_score += successive
    test_scores.append(test_score)
for score in test_scores:
    print(score)