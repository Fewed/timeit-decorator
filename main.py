from time import time as __time

__limit = 40


def __sep_by_3(num):
    st = str(num)
    temp = ''
    for idx, char in enumerate(st):
        temp += ('', ' ')[idx % 3 == 0] + st[-1 - idx]
    return temp[::-1].strip()


def ti(cycles=1):
    def wrapper(fun):
        def internal(*args):
            rng = range(cycles)
            start = __time()
            for i in rng:
                fun(*args)
            end = __time()
            t_ns = round(1e9 * (end - start) / cycles)
            if (len(str(args))) > __limit:
                args_str = f'{str(args)[:__limit]}...{str(args)[-__limit:]}'
            else:
                args_str = str(args)
            print(f'{fun.__name__}{args_str} executed in {__sep_by_3(t_ns)} ns'.replace(',)', ')'))

        return internal

    return wrapper
