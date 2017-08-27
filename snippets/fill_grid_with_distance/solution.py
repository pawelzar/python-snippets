def dist(a, b):
    """Returns Manhattan distance between point a and b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def grid_with_distance(width, height, point_a, point_b):
    """
    Returns grid in which every cell means either it is
    closer to point 1 or point 2.
    """
    grid = []

    for y in range(height):
        line = ''
        for x in range(width):
            dist_a = dist((x, y), point_a)
            dist_b = dist((x, y), point_b)
            if (x, y) == point_a or (x, y) == point_b:
                line += 'X'
            else:
                if dist_a < dist_b:
                    line += '1'
                elif dist_a > dist_b:
                    line += '2'
                else:
                    line += '0'
        grid.append(line)

    return grid


if __name__ == '__main__':
    width, height = [int(i) for i in input().split()]
    point_1 = [int(i) for i in input().split()]
    point_2 = [int(i) for i in input().split()]

    print('\n'.join(grid_with_distance(width, height, point_1, point_2)))
