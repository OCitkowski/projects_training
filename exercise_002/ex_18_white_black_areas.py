def white_black_areas_best(cs, rs):
    r_even, r_odd = sum(rs[1::2]), sum(rs[::2])
    c_even, c_odd = sum(cs[1::2]), sum(cs[::2])
    return (c_odd * r_odd + c_even * r_even, r_even * c_odd + r_odd * c_even)

def white_black_areas(cs: list, rs: list) -> tuple:
    cs_white = [cs[i] for i in range(len(cs)) if i%2 == 0]
    cs_black = [cs[i] for i in range(len(cs)) if i%2 != 0]

    rs_white = [rs[i] for i in range(len(rs)) if i%2 == 0]
    rs_black = [rs[i] for i in range(len(rs)) if i%2 != 0]

    total_white_area = sum(cs_white) * sum(rs_white) + sum(cs_black) * sum(rs_black)
    total_black_area = sum(cs_white) * sum(rs_black) + sum(cs_black) * sum(rs_white)
    #
    # print(cs_white, cs_black)
    # print(rs_white, rs_black)
    # print(sum(cs_white), sum(rs_white), sum(cs_black), sum(rs_black))
    # print(total_white_area, total_black_area)

    return (total_white_area, total_black_area)

def white_black_areas_3(cs: list, rs: list) -> tuple:
    total_white_area = 0
    total_black_area = 0
    # matrix = [[cs[i] * rs[j] for i in range(len(cs))] for j in range(len(rs))]
    # # matrix2 = ([cs[i] * rs[j] for i in range(len(cs))] for j in range(len(rs)))
    # # matrix2 = ((cs[i] * rs[j] for i in range(len(cs))) for j in range(len(rs)))
    #
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(matrix[i][j])
    # # print(f'{matrix}')
    # print(f'{matrix2} {matrix2}')
    print(cs * 3)
    return (total_white_area, total_black_area)

def white_black_areas_2(cs: list, rs: list) -> tuple:

    total_white_area = sum((cs[i] * rs[j] for i in range(len(cs)) for j in range(len(rs)) if
                  (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)))
    total_black_area = sum((cs[i] * rs[j] for i in range(len(cs)) for j in range(len(rs)) if
                  (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0)))

    print(f'total_white_area - {total_white_area}  / total_black_area - {total_black_area} ')
    return (total_white_area, total_black_area)

def white_black_areas_old(cs: list, rs: list) -> tuple:
    """# Execution Timed Out (12000 ms)
        https://www.codewars.com/kata/6262f9f7afc4729d8f5bef48/train/python
        # return a 2-element tuple, (total_white_area, total_black_area)
        # List cs contains the N widths of the N columns of the chessboard
        # List rs contains the N heights of the N rows of the chessboard
        # Remember, board coloring starts with top left cell => WHITE
        # and then alternates with BLACK as in a usual chessboard."""
    total_white_area = 0
    total_black_area = 0
    for i in range(len(cs)):
        for j in range(len(rs)):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                total_white_area += cs[i] * rs[j]
            else:
                total_black_area += cs[i] * rs[j]

    print(f'total_white_area - {total_white_area}  / total_black_area - {total_black_area}')

    return (total_white_area, total_black_area)

if __name__ == '__main__':

    assert white_black_areas([3, 1, 2, 7, 1], [1, 8, 4, 5, 2]) == (146, 134)
    # assert white_black_areas([3], [2]) == (6, 0)