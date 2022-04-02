def xbonacci(signature, n):

    len_sign = len(signature)
    # for i in range(0, n):
    #
    #     if i >= len_sign and i < n:
    #         signature.append(sum(signature[i - len_sign: i]))
    #     print(f'i - {i} / n - {n} / {signature}')
    [signature.append(sum(signature[i - len_sign: i])) for i in range(0, n) if i >= len_sign]
    return signature[0 : n]

def Xbonacci_Best(signature,n):
    return signature[:1] + Xbonacci_Best(signature[1:] + [sum(signature)], n-1) if n else []

if __name__ == '__main__':

    assert xbonacci([0, 1], 10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert xbonacci([16, 14, 20, 11, 7, 17, 3, 3, 15, 2, 5, 20], 3) == [16, 14, 20]

