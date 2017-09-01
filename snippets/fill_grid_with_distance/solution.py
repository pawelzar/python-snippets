def grid_with_distance(width, height, point_1, point_2):
    """
    Fill the grid with cells that mean either they are
    closer to the first or the second point.

    :param width: width of the grid
    :param height: height of the grid
    :param point_1: coordinates of first point
    :param point_2: coordinates of second point
    :return: grid represented as list of strings
    """
    grid = []
    closer = {0: '0', 1: '1'}

    for y in range(height):
        line = ''
        for x in range(width):
            if (x, y) == point_1 or (x, y) == point_2:
                line += 'X'
            else:
                dist_1 = manhattan_distance((x, y), point_1)
                dist_2 = manhattan_distance((x, y), point_2)
                compare = (dist_1 < dist_2) - (dist_1 > dist_2)
                line += closer.get(compare, '2')
        grid.append(line)

    return grid


def manhattan_distance(point_1, point_2):
    """
    Compute Manhattan distance between two points. That is a distance on a
    strictly horizontal and/or vertical path.

    :param point_1: coordinates of first points
    :param point_2:coordinates of second point
    :return: distance between two points as integer
    """
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


if __name__ == '__main__':
    WIDTH, HEIGHT = [int(i) for i in input().split()]
    POINT_1 = [int(i) for i in input().split()]
    POINT_2 = [int(i) for i in input().split()]

    print('\n'.join(grid_with_distance(WIDTH, HEIGHT, POINT_1, POINT_2)))
