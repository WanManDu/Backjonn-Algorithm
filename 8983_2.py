import sys

def hunted_animals(start, end, dist, hunters, animals):
    if start > end:
        return end
    
    for animal in animals:
        dist = L - animal[1]

        mid = (start + end) // 2
        hunted_animals = 0

        while start <= end:
            mid = (start + end) // 2

            if hunters[mid] < animal[0] - dist:
                return hunted_animals(mid + 1, end, dist, hunters, animals)
            if hunters[mid] > animal[0] + dist:
                return hunted_animals(start, mid - 1, dist, hunters, animals)
            else:
                hunted_animals += 1
                return hunted_animals


M, N, L = map(int, sys.stdin.readline().split())

Hunter_location = list(map(int, sys.stdin.readline().split()))

Animal_location = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Hunter_location.sort()


H = hunted_animals(0, len(Hunter_location) - 1, L, Hunter_location, Animal_location)
print(H)