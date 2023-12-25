from numpy.compat import long


# функция-декоратор
def decor_fib_cache(func):
    cache = {}  # создание нового словаря для каждой декорируемой функции

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            return result

    return wrapper


@decor_fib_cache
def calc_fib(n) -> long:
    if n < 2:
        result = n
    else:
        result = calc_fib(n - 1) + calc_fib(n - 2)
    return result


if __name__ == '__main__':
    num: int = 11
    fib_value = calc_fib(num)
    print(fib_value)
