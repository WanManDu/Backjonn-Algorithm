

def black_game(card_lists, depth, used, score):
    #depth가 k일 떄, card_lists에 cards[i]를 추가하고 used[i]를 True로 하면 재귀함수 끝남
    if depth == 3:
        #card_lists 에 있는 숫자중 중복되지 않게 numbers에 추가
        card_lists = sorted(card_lists)  #순서가 다른 같은 조합을 동일하게 인식하기 위해 정렬
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