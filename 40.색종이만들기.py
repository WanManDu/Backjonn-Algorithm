import sys


#x : 가로 정사각형의 좌표 
#y : 세로 정사각형의 좌표

def paper_slice(x, y, N):
    global white_square, blue_square

    #color : 가장 작은 단위의 정사각형의 색깔
    color = square_color[x][y]

    for i in range(x, x+N):
        for j in range(y, y + N):
            if color != square_color[i][j]:
                paper_slice(x, y, N // 2)
                paper_slice(x, y + N // 2, N // 2)
                paper_slice(x + N // 2, y, N // 2)
                paper_slice(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white_square += 1
    else:
        blue_square += 1

#정사각형의 가로 세로 길이를 입력
N = int(sys.stdin.readline())

#가로 1 세로 1의 길이를 가진 가장 작은 정사각형의 색깔을 입력
square_color = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

#파란색으로 이루어진 정사각형과 하얀색으로 이루어진 정사각형의 개수
blue_square = 0
white_square = 0

#(0, 0)부터 시작
paper_slice(0, 0, N)
print(white_square)
print(blue_square)

