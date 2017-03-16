def my_counter(n):
    i = 0
    while i < n:
        yield i
        i += 1

def main():
    for x in my_counter(5):
        print(x)


if __name__ == '__main__':
    main()