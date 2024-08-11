import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
wordList = []

for i in range(n):
    word = input().strip()
    ascii_values = []

    for char in word:
        ascii_values.append(ord(char))

    wordList.append(ascii_values)

for i in range(len(wordList)):


for i in range(len(wordList)):
    word_string = ""
    for j in wordList[i]:
        word_string += chr(j)
    print(word_string)


