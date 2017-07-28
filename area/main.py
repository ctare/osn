#! cat input | python3 main.py

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
rects = [r1, r2]

result = 0

def create_area(rects):
    startX = min(rects, key=lambda x: x[0])[0]
    startY = min(rects, key=lambda x: x[1])[1]
    endX = max(rects, key=lambda x: x[2])[2]
    endY = max(rects, key=lambda x: x[3])[3]
    return [[0 for x in range(endX - startX)] for y in range(endY - startY)], [startX, startY]


def fill_area(rects, area, diff):
    diffX, diffY = diff
    for r in rects:
        for y in range(r[1], r[3]):
            for x in range(r[0], r[2]):
                area[y - diffY][x - diffX] = 1


def calc_area(area):
    return sum(sum(row) for row in area)


area, diff = create_area(rects)
fill_area(rects, area, diff)
print(area)
print(calc_area(area))
for row in area:
    print(row)
