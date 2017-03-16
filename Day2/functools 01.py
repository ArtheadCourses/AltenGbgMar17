from functools import partial

def power(base, pow):
    return base**pow

def square(n):
    return power(n,2)

def cube(n):
    return power(n,3)

def func_fact(pow):
    def inner(base):
        return base**pow
    return inner

def main():
    s1 = func_fact(2)
    c1 = func_fact(3)

    print(square(2))
    print(cube(2))

    s2 = partial(power, pow=2)
    c2 = partial(power, pow=3)

    print(s2(2))
    print(c2(2))

    f = lambda b, p: b**p
    s3 = partial(f,b=33, p=2)
    c3 = partial(f, p=3)

    print(s3())
    print(c3(2))


if __name__ == '__main__':
    main()