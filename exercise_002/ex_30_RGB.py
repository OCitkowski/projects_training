def rgb_my_kata(r, g, b):
    def one_rgb(one):
        if one < 0:
            one = 0
        elif one > 255:
            one = 255

        one_str_hex = f'{str(hex(one)).replace("x", "")}'
        one_str_hex = one_str_hex[-2].upper() + one_str_hex[-1].upper()
        return one_str_hex

    print(f'{one_rgb(r)}{one_rgb(g)}{one_rgb(b)}')
    return f'{one_rgb(r)}{one_rgb(g)}{one_rgb(b)}'


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    # print(("{:02X}" * 3).format(round(r), round(g), round(b)))
    # print(f'{round(r)}, {round(g)}, {round(b)}')
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


if __name__ == '__main__':
    # assert (rgb(["OXO", "XXX", "OXO", "OXX", "O0X", "X0O"]) == "Total land perimeter: 22")

    rgb(0, 0, 0)
    rgb(255, 255, 256)
    rgb(1, 2, 3)

    assert (rgb(0, 0, 0) == "000000")
    assert (rgb(1, 2, 3) == "010203")
    assert (rgb(255, 255, 255) == "FFFFFF")
    assert (rgb(254, 253, 252) == "FEFDFC")
    assert (rgb(-20, 275, 125) == "00FF7D")
