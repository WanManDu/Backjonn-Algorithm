A, B, V= map(int, input().split())

#달팽이가 낮이 끌날때 도착지점에 도착하는 경우
if (V - A) % (A - B) == 0:
    print((V - A) // (A - B) + 1)
#달팽이가 낮 중에 도착지점에 도착하는 경우
else:
    print((V - A) // (A - B) + 2)