
n = 4
x1 = lambda x = n: x**2

my_list_x = 'kjgkjigkjghkjg'
x2 = lambda my_list = my_list_x: [i for i in my_list]

x3 = lambda: 'jufgjhgkjghjg'

x4 = lambda : x**2



if __name__ == '__main__':
    # print(x1())
    #
    # my_1 = '1111111111111111'
    # print(x2(my_1))
    #
    # my_1 = '1111112222222222'
    # print(x2(my_1))
    #
    # my_2 = '2222222222222222'
    # print(x2(my_2))
    # print(x2())
    # print(x3())
    #
    # x = 2
    # print(f'{x4()}')
    # x = 3
    # print(f'{x4()}')

    # for i in range(10):
    #     result = lambda: i**2
    #     print(result())

    ints = list(range(100))
    for i in filter(lambda x: x % 2 == 0, ints):
        print(i)
