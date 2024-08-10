import sys

input = sys.stdin.readline

def search_by_z(num, row, column):
    #점화식으로 따지면 T(1)값
    if num == 1:
        return 2 * row + column
    
    #큰 정사각형을 4등분함
    #왼쪽 위의 정사각형을 part1, 오른쪽 위의 정사각형을 part2
    #왼쪽 아래의 정사각형을 part3, 오른쪽 아래의 정사각형을 part4   

    #part1
    if row < 2 ** (num - 1) and column < 2 ** (num - 1):
        return search_by_z(num - 1, row, column)

    #part2
    if row < 2 ** (num - 1) and column >= 2 ** (num - 1):
        return 1 * 2 ** (2 * num - 2) + search_by_z(num - 1, row, column - 2 ** (num - 1))
    #part3
    if row >= 2 ** (num - 1) and column < 2 ** (num - 1):
        return 2 * 2 ** (2 * num - 2) + search_by_z(num - 1, row - 2 ** (num - 1), column)
    #part4
    else:
        return 3 * 2 ** (2 * num - 2) + search_by_z(num - 1, row - 2 ** (num - 1), column - 2 ** (num - 1))
    
    #sarch_by_z(n, r, c)에서 인자들이 바뀌는 이유는
    #모두 part1과 같은 위치로 옮기기 위해서이다.
    #part3를 예로 들어보면, row > = 2 **(num - 1)이므로
    #search_by_z(n, row - 2 ** (num - 1), column)을 해주면
    #row의 값은 part1에서의 row 범위 안으로 들어온다.
    
n, r, c = map(int, input().split())

print(search_by_z(n, r, c))


#