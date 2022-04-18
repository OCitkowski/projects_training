def diamond(n: int) -> str:
    if n % 2 == 0 or n <= 0:
        return None

    result = '\n'.join(
        [f'{" " * (abs(n - x) // 2)}{"*" * (n - (abs(n - x)))}' for x in range(2 * n) if x % 2 != 0]) + "\n"
    return result

diamond=lambda n: list(map(lambda s: ''.join(s+s[::-1][1:]),[[((n-i)//2)*' '+i*'*'+str('\n') for i in range(1,n+1,2)]]))[0] if n>0 and n%2 else None

if __name__ == '__main__':
    print(f'{diamond(5)}')
