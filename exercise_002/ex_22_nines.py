def nines_old(n):
    # number_of_nines = []
    result = 0
    for i in range(n):
        y = str(i).split('9')
        if len(y) > 1:
            # number_of_nines.append(i)
            result += 1
    return result


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'start- {start} / end- {end} / seconds- {end - start} ')
        return return_value

    return wrapper


@benchmark
def nines(n):
    coefficient = len(str(n))
    number_with_nines = [i for i in range(9, n, 10) if str(i).find('9') >= 0]
    y = []
    for i in range(coefficient - 1):
        x = [i for i in range(int('9' + '0' * i), n, 1) if str(i).find('9') >= 0]  # 99
        y += x
    number_with_nines += y

    # print(number_with_nines)

    return len(set(number_with_nines))


if __name__ == '__main__':
    # print(f'{nines(1)}')
    print(f'{nines(39500000)}')
    # print(f'{nines(1000)}')
    # print(f'{nines(3950)}')
    # self.assertEqual(nines(10), 1, "With n = 10")
    # self.assertEqual(nines(100), 19, "With n = 100")
    # self.assertEqual(nines(1000), 271, "With n = 1000")
    # self.assertEqual(nines(3950), 1035, "With n = 3950")
