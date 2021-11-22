def gen_fun(n=5):
    i = 0
    while i <= n:
        i += 1
        yield i

def main():
    a = gen_fun()
    for i in a:
        print(i)

    l = [1, 2, 3, 4]
    l = iter(l)
    try:
        print(next(l))
        print(next(l))
        print(next(l))
        print(next(l))
        print(next(l))
    except StopIteration:
        print("Out of elements")
   




if __name__ == "__main__":
    main()