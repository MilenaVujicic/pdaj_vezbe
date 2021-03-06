import multiprocessing as mp
import time

def pause(x):
    time.sleep(x)
    return x

def main():
    p = mp.Pool()
    star_time = time.time()
    res = p.imap_unordered(pause, [1, 5, 3])
    for r in res:
        print("{} time elapsed {}s".format(r, int(time.time() - star_time)))
    p.terminate()
if __name__=="__main__":
    main()