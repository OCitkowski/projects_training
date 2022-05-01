def min_permutation(n: int) -> int:
    """Given a number, find the permutation with the smallest absolute value (no leading zeros)."""

    n_list = sorted(list(str(n)))
    for i in range(len(n_list)):
        if n_list[i] != '0' and n_list[i] != '-':
            x = n_list.pop(i)
            n_list.insert(0, x) if '-' not in n_list else n_list.insert(1, x)
            break
    result = int(''.join(n_list))
    return result

def min_permutation_best(n):
    f = n < 0
    s = "".join(sorted(str(abs(n))))
    n = s.count("0")
    s = s.replace("0", "")
    return int(s[:1] + "0" * n + s[1:]) * (-1 if f else 1)

def min_permutation_best2(n):
    s = ''.join(sorted(str(abs(n))))
    i = next((i for i,c in enumerate(s) if c!='0'), len(s))
    v = int(s[i:i+1] + s[:i] + s[i+1:])
    return -v if n<0 else v


if __name__ == '__main__':

    assert min_permutation(-987645231) == -123456789
    # assert min_permutation(-9876452310) == -1234567890
    assert min_permutation(-20) == -20
    assert min_permutation(0) == 0
    assert min_permutation(10) == 10
    assert min_permutation(29394) == 23499
