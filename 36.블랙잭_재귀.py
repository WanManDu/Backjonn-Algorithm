

def black_game(card_lists, depth, used, score):
    #depth == 3일때, 기저조건 실행
    if depth == 3:
        personal_score = sum(card_lists)
        if personal_score <= M:
            score.append(personal_score)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            black_game(card_lists + [cardList[i]], depth + 1, used, score)
            used[i] = False

N, M = map(int, input().split())

#카드 숫자 입력. n번 입력을 받아 각 입력값을 문자열로 리스트에 저장. 
cardList = list(map(int, input().split()))

#카드로 만들어진 조합 저장할 리스트

score = []
#재귀함수를 호출하고 끝내기 위해 만듬
used = [False] * N

#재귀함수 호출
black_game([], 0, used, score)

print(max(score))