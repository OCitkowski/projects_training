def get_drinks(number_of_guests: int) -> int:
    # write your code here
    i, result = 0, 0

    while i < number_of_guests:
        i += 1
        result += i

    return result


def get_drinks_with_step(number_of_guests: int, step: int) -> int:
    result = 0

    for i in range(1, number_of_guests + 1, step):
        result += i
        print(i)
    return result



if __name__ == "__main__":
    print(get_drinks_with_step(10, 3))
