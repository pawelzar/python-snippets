The program:
Given the coordinates of the points 1 and 2, fill the grid of the given size in order to indicate which character is the closest. We will use here the Manhattan distance: d(A, B) = abs(Ax - Bx) + abs(Ay - By).

Display a grid that contains, in each cell, the character:
- 'X' if a point is in the cell
- '0' if the cell is equidistant to the two points
- '1' if the closest point to the cell is point 1
- '2' if the closest point to the cell is point 2

INPUT:
Line 1 : two space separated integers giving the width and the height of the grid
Line 2 : two space separated integers giving the coordinates of point 1
Line 3 : two space separated integers giving the coordinates of point 2

OUTPUT:
A grid of height lines of width characters that respects the rules.

CONSTRAINTS:
1 < width, height ≤ 200
0 ≤ x1, y1, x2, y2 < 200

EXAMPLE:
Input
10 10
4 5
8 7
Output
1111111022
1111111022
1111111022
1111111022
1111111022
1111X11022
1111110222
11111022X2
1111102222
1111102222


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

width, height = [int(i) for i in raw_input().split()]
point_1 = [int(i) for i in raw_input().split()]
point_2 = [int(i) for i in raw_input().split()]

for y in range(height):
    line = ""
    for x in range(width):
        dist_1 = dist((x, y), point_1)
        dist_2 = dist((x, y), point_2)
        if [x, y] == point_1 or [x, y] == point_2:
            line += "X"
        else:
            if dist_1 < dist_2:
                line += "1"
            elif dist_1 > dist_2:
                line += "2"
            else:
                line += "0"
    print line
