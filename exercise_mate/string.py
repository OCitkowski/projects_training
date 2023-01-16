# # "NASA"
# make_abbr("national aeronautics space administration")
# # "CPU"
# make_abbr("central processing unit")
# # "SMILES"
# make_abbr("simplified molecular input line entry specification")

def make_abbr(words: str) -> str:
    result = ""
    if len(words) != 0:
        for word in words.upper().split(" "):
            result += word[0]
    return result


def decrypt_message(message: str) -> str:
    l_message = list(message)
    result = ""
    for i in range(len(l_message), 0, -1):
        result += l_message[i - 1]
        # print(l_message[i - 1])

    return result


def is_werewolf(target: str) -> bool:
    target = target.translate({ord(i): None for i in '123,."[]?()!<>~@#$%^&*()_+=-1234567890;: '}).lower()
    l_message = list(target.upper().replace(' ', ""))
    result = ""

    for i in range(len(l_message), 0, -1):
        result += l_message[i - 1]

    l_result = list(result)

    return l_result == l_message


def get_success_rate(statistics: str) -> int:
    if len(statistics.replace(' ', "")) == 0:
        return 0
    all_st = len(statistics)
    success_st = len(statistics.replace('0', ""))
    return round(success_st / all_st * 100)


if __name__ == "__main__":
    print(get_success_rate("11100"))  # 60
    print(get_success_rate("1100"))  # 50
    print(get_success_rate(" "))  # 50
