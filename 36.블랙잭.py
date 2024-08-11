

def black_game(card_lists, depth, used, numbers):
    #depth가 k일 떄, card_lists에 cards[i]를 추가하고 used[i]를 True로 하면 재귀함수 끝남
    if depth == M:
        #card_lists 에 있는 숫자중 중복되지 않게 numbers에 추가
        if card_lists not in numbers:
            numbers.append(card_lists)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            black_game(card_lists + cards[i], depth + 1, used, numbers)
            used[i] = False

N = int(input())

M = int(input())

#카드 숫자 입력. n번 입력을 받아 각 입력값을 문자열로 리스트에 저장. 
cards = [input().strip() for _ in range(N)]

#카드로 만들어진 조합 저장할 리스트
numbers = []

#재귀함수를 호출하고 끝내기 위해 만듬
used = [False] * N

#재귀함수 호출
black_game("", 0, used, numbers)

print(sum(numbers))