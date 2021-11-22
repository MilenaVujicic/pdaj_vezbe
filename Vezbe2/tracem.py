import tracemalloc
from math import sqrt

def gen_list(n):
    return list(range(1, n+1))

def is_square_c(l):

    return [r for r in l if sqrt(r).is_integer()]

def is_square_y(l):
    for i in range(1, l+1):
        if sqrt(i).is_integer():
            yield i

def double_loop(n, m):
    res = []
    for i in range(0, n):
        for j in range(0, m):
            res.append(i+j)
    return res


def main():

    #res = is_square(gen_list(100000000))
    tracemalloc.start()
    res = is_square_c(gen_list(100000))
    current, peak = tracemalloc.get_traced_memory()
    print(f"[Comp] Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

    tracemalloc.start()
    a = is_square_y(100000)
    for i in a:
        pass
    current, peak = tracemalloc.get_traced_memory()
    print(f"[Gen] Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()