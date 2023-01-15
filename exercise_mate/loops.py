def print_numbers(n: int) -> None:
    i = 0
    while i <= n - 1:
        print(i)
        i += 1
    return i


if __name__ == "__main__":
    print_numbers(10)
    print_numbers(1)
    print_numbers(0)
