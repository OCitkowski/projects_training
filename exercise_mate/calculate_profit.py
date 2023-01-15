from typing import Union


def calculate_profit(amount: int, percent: Union[float, int], period: int) -> int:
    start_amount = amount
    for i in range(0, period):
        amount_percent = amount * percent / 100
        amount += amount_percent

    return int(amount - start_amount)


if __name__ == "__main__":
    print(calculate_profit(1110, 10, 0))
    print(calculate_profit(12500, 3, 12))  # 5322
    print(calculate_profit(10000, 4, 3))  #

