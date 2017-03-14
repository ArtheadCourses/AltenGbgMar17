class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


def main():
    c = Counter(4, 9)
    for i in c:
        print('one',i)

    for i in c:
        print('two',i)

    it = iter(Counter(2,6))
    #print(next(it))

    c2 = Counter(5,19)
    for i in c2:
        if i == 9:
            break

    l = list(c2)
    print(l)
    print(next(c2))


if __name__ == '__main__':
    main()