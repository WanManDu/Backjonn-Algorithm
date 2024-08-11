import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
wordSet = set()

# 단어 입력
for i in range(n):
    word = input().strip()  # 개행 문자 제거
    wordSet.add(word)  # 중복을 허용하지 않는 set에 추가

# 단어 길이와 알파벳 순서를 고려하여 정렬
#key : lambda는 정렬 조건을 만들 거라는 걸 알리는것
# (len(x), x)는 단어의 길이를 먼저 정렬하고, 단어의 알파벳순서에 따라 정렬한다는 것
wordList = sorted(wordSet, key=lambda x: (len(x), x))

# 정렬된 단어 출력
for word in wordList:
    print(word + '\n')
