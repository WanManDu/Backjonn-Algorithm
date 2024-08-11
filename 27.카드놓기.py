#카드 조합 생성 함수
#card_lists : 현재까지 선택한 카드들의 조합을 저장
#depth : 현재까지 몇개의 카드를 선택했는지를 확인
#used : 각 카드가 현재 조합에서 사용되었는지 확인
#numbers : 현재까지 생성된 중복되지 않는 숫자의 조합을 저장

def card_game(card_lists, depth, numbers):
    #depth가 k일 떄, card_lists에 cards[i]를 추가하고 used[i]를 True로 하면 재귀함수 끝남
    #card_lists에는 바로 숫자로 저장됨. 예를 들면, '2', '25' '5'를 조합해서 '2255', '2525', '5225' 등이 numbers에 저장됌
    #이를 위해 card_lists에 리스트 [] 대신 "" 문자열을 사용하는 것.
    if depth == k:
        #card_lists 에 있는 숫자중 중복되지 않게 numbers에 추가
        if card_lists not in numbers:
            numbers.append(card_lists)
        return
    
    for i in range(n):
        card_game(card_lists + cards[i], depth + 1, numbers)


#카드 개수 입력
n = int(input())
#전체 카드 중 고를 카드의 개수 입력
k = int(input())

#카드 숫자 입력. n번 입력을 받아 각 입력값을 문자열로 리스트에 저장. 
cards = [input().strip() for _ in range(n)]

#카드로 만들어진 조합 저장할 리스트
numbers = []

#재귀함수를 호출하고 끝내기 위해 만듬
used = [False] * n

#재귀함수 호출
card_game("", 0, numbers)

print(len(numbers))