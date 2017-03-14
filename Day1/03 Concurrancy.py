from multiprocessing import Pool

def f(x):
    return x*x

def main():
    with Pool(5) as p:
        print(p.map(f, range(100)))


if __name__ == '__main__':
    main()