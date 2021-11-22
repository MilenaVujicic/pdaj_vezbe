def main():
    l = [1, 2, 3, 5, 6, 10, 10, 6, 6]
    nova_l = []
    for num in l:
        if num % 2 == 0 and num != 10:
            nova_l.append(num)
    #print(nova_l)

    nova_l = [num for num in l if num%2==0 and num != 10]
    #print(nova_l)

    nova_l = [(num, num**2) for num in l if num%2==0 and num != 10]
    #print(nova_l)

    d = {"a":2, "b":3, "c":5, "d":8}
    novi_d = {k:v for (k, v) in d.items() if v%2==0}
    #print(novi_d)

    l = [1, 2, 3, 5, 6, 10, 10, 6, 6]
    res = [(num, i) for (i, num) in enumerate(l)]
    print(res)

    l2 = [2, 3]

    res = [a+b for a in l for b in l2 if a%2==0 and b%2!=0]
    print(res)

if __name__ == "__main__":
    main()