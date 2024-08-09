#min함수를 쓰지 않고 week1-6.py 만들기

x, y ,w, h = map(int, input().split())

min = abs(x)
if min > abs(y): min = abs(y)
if min > abs(w-x): min = abs(w-x)
if min > abs(h-y): min = abs(h-y)

print(min)