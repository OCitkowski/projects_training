result = None
number_of_iterations = 0


def amount_of_pages_old(summary: int, amound_dict: dict = None) -> int:
    global result
    global number_of_iterations

    computed = lambda num: (len(''.join([str(i) for i in range(1, num + 1)])))

    if amound_dict == None:
        amound_dict = {}
        amound_dict['number_of_iterations'] = 0
        amound_dict['num_min'] = summary // int(len(str(summary)))
        amound_dict['num_max'] = summary if summary < 1000 else summary // 2
        amound_dict['sum_min'] = computed(amound_dict['num_min'])
        amound_dict['sum_max'] = computed(amound_dict['num_max'])

    amound_dict['number_of_iterations'] += 1

    if amound_dict['number_of_iterations'] == 10:
        return result

    num = (amound_dict['num_min'] + amound_dict['num_max']) // 2
    sum = computed(num)

    if sum == summary:
        amound_dict['sum_min'] = sum
        amound_dict['num_min'] = num
        result = amound_dict['num_min']
        print(f' iteration {amound_dict["number_of_iterations"]}')
        print(
            f' result {result} // summary {summary} '
            f'// sum_min/sum_max - {amound_dict["sum_min"]} / {amound_dict["sum_max"]} ')
        return result

    if sum > summary:
        amound_dict['num_max'] = num
        amound_dict['sum_max'] = sum

    if sum < summary:
        amound_dict['sum_min'] = sum
        amound_dict['num_min'] = num

    amount_of_pages(summary, amound_dict)

    return result

def amount_of_pages(summary: int) -> int:
    # calculate_old = lambda num: (len(''.join([str(i) for i in range(1, num + 1)])))
    # calc_string = f'({summary}'
    # len_sum = len(str(summary))
    # for i in range(0, len_sum):
    #     if i != len_sum - 1:
    #         calc_string += ' - '
    #         calc_string += '9' + '0' * i + '*' + f'{i + 1}'
    #     else:
    #         if len_sum == 1:
    #             calc_string += ')'
    #         else:
    #             calc_string += f') // {len_sum} + {"9" * (len_sum - 1)}'
    # result = eval(calc_string)

    # print(f'{calc_string} ----- res {result} // sum {summary} == {calculate_old(result)}')
    return None

if __name__ == '__main__':                                                                                                                                                                                                                                                                                                        amount_of_pages(1095)
    amount_of_pages(5)
    # assert amount_of_pages(5) == 5
    # assert amount_of_pages(25) == 17
    # assert amount_of_pages(185) == 97
    # assert amount_of_pages(660) == 256
    # assert amount_of_pages(1095) == 401
    # assert amount_of_pages(2893) == 1000
