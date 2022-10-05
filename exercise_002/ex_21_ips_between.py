from ipaddress import ip_address


def best_1_ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)


def ips_between(start, end):

    start_list = start.split('.')
    end_list = end.split('.')
    full_result = 0
    coof = [256**i for i in range(3, -1, -1)]
    for i in range(4):

        result =  (int(end_list[i]) - int(start_list[i])) * coof[i]
        full_result += result
        # print(f' {int(end_list[i])} - {int(start_list[i])}  * {coof[i]} // i = {i}// {result} //{i}')
    # print(f'{full_result} start = {start} end = {end} coof = {coof}')
    return full_result



if __name__ == '__main__':
    # ips_between("20.0.0.10", "20.0.1.0")
    ips_between("170.0.0.0", "170.1.0.0")
    ips_between("50.0.0.0", "50.1.1.1")
    # assert ips_between("20.0.0.10", "20.0.1.0") == 246
    # self.assertEqual(ips_between("170.0.0.0", "170.1.0.0"), 65536)
    # self.assertEqual(ips_between("50.0.0.0", "50.1.1.1"), 65793)