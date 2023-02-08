def land_perimeter(arr):
    total_land_perimeter = 0
    row_count = 0

    for row in arr:
        column_count = 0
        print('-----')
        for symbol in row:

            if symbol == 'X':
                p = 4
            else:
                print('0')
                column_count += 1
                continue

            if row_count != 0 and arr[row_count - 1][column_count] == 'X':
                p -= 2

            if column_count != 0 and row[column_count - 1] == 'X':
                p -= 2

            total_land_perimeter += p
            print(total_land_perimeter)

            column_count += 1
        row_count += 1
        # print(total_land_perimeter)

    return f'Total land perimeter: {total_land_perimeter}'


if __name__ == '__main__':
    # assert (land_perimeter(["OXO", "XXX", "OXO"]) == "Total land perimeter: 12")
    # assert (land_perimeter(["OXO", "XXX", "O0O"]) == "Total land perimeter: 10")
    assert (land_perimeter(["OXO", "XXX", "OXO", "OXX", "O0X", "X0O"]) == "Total land perimeter: 22")

    # assert (land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO",
    #                         "OXOOXX"]) == "Total land perimeter: 60")

    # test.assert_equals(land_perimeter(
    #     ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]),
    #                    "Total land perimeter: 60")
    # test.assert_equals(land_perimeter(
    #     ["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]),
    #                    "Total land perimeter: 52")
    # test.assert_equals(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]),
    #                    "Total land perimeter: 40")
    # test.assert_equals(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]),
    #                    "Total land perimeter: 54")
    # test.assert_equals(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]),
    #                    "Total land perimeter: 40")
