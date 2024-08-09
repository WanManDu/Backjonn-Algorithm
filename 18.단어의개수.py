text = input()
words = text.split() #split(" ")을 사용하면 하나의 공백을 기준으로 나누기 때문에, 공백이 여러개 연속으로 나오게 된다.
result = len(words)
print(words)
print(result)