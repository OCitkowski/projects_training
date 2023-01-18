def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i*i
    return result


# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

if __name__ == '__main__':
    assert(square_sum([1, 2]) == 6)
    assert(square_sum([0, 3, 4, 5]) == 50)
    assert(square_sum([]) == 0)
    assert(square_sum([-1, -2]) == 5)
    assert(square_sum([-1, 0, 1]) == 2)
#your code here

