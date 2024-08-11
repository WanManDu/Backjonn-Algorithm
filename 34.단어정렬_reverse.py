import sys
input = sys.stdin.readline
print = sys.stdout.write

#입력한 단어를 길이가 길고, 알파벳 순위가 늦은 순서대로 출력

n = int(input())
wordSet = set()

# 단어 입력
for i in range(n):
    word = input().strip()  # 개행 문자 제거
    wordSet.add(word)  # 중복을 허용하지 않는 set에 추가

# 단어 길이와 사전 반대 순서를 고려하여 정렬
#''.join은 알파벳들을 합쳐 하나의 문자열로 만들기 위해 사용
#chr(255-ord(c))는 원래의 알파벳 순서를 반대로 하기위해 사용. 
#for c in x는 단어 속의 각 알파벳 순서를 모두 반대로 하기위해 사용. c가 알파벳. x가 단어
#key = lambad 뒤는 정렬 기준일 뿐 변환된 단어를 저장하진 않음.
wordList = sorted(wordSet, key=lambda x: (-len(x), ''.join(chr(255 - ord(c)) for c in x)))

# 정렬된 단어 출력
for word in wordList:
    print(word + '\n')
