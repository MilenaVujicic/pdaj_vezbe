import multiprocessing as mp
import tracemalloc
from os import cpu_count

def square_function(num):
    ret = []
    for i in range(num):
        ret.append(i**2)
    return ret


def square_by_two(num):
    li = square_function(num)
    ret = []
    for l in li:
        ret.append(l/2)
    return ret


def main():

    tracemalloc.start()
    with mp.Pool() as pool:
        res = pool.map(square_by_two, range(10000), chunksize=10**3)
        for r in res:
            #print(r)
            pass

    #res = square_by_two(15000000)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
    tracemalloc.stop()


if __name__ == "__main__":
    main()