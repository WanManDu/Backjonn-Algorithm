def solve(a):
    result = 0
    for i in range(len(a)):
        result += a[i]
    return result

a=[1, 2, 3, 4, 5]
print(solve(a))

#def solve(a: list) -> int;
#   reutrn sum(a)