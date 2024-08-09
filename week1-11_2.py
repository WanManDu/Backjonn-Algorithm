a=[]

for i in range(9):
    i=int(input())
    a.append(i)

max=max(a)
print(max)
print(a.index(max)+1)