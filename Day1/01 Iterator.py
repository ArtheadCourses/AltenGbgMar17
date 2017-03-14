def main():
    num = [1, 2, 3, 4]
    print(next(num.__iter__()))
    print(next(num.__iter__()))

    it = iter(num)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

if __name__ == '__main__':
    main()