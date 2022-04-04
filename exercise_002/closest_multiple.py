# Given a number return the closest number to it that is divisible by 10.
#
# Example input:
#
# 22
# 25
# 37
#
# Expected output:
#
# 20
# 30
# 40


def closest_multiple_10(i):

    x, y = int(i) // 10, int(i) % 10
    x *= 10
    if y >= 5:
        x += 10
    return x

def bestpr_closest_multiple_10(i):
    return round(i, -1)

if __name__ == '__main__':
    assert closest_multiple_10(55) == 60
