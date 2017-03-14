import itertools


def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))


def create_lists(iterable, num_per_list):
    return list(split_seq(iterable, num_per_list))


def main():
    my_list = [34, 56, 12, 56, 45, 34, 22, 78, 64, 52]
    result = create_lists(range(10), 2) # [[0,1],[2,3],[4,5],[6,7],[8,9]]
    print(result)


if __name__ == '__main__':
    main()