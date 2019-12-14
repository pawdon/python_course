def triangle(h: int, a: int, char='*'):
    for i in range(1, h + 1):
        x = round(i * a / h)
        if x == 0:
            x = 1
        print(char * x)


def fib(n: int) -> int:
    if n < 0:
        raise ValueError('n < 0')
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

