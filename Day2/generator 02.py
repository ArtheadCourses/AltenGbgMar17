def my_counter(it):
    yield from it

def my_counter2(it):
    for value in it:
        yield value

def main():
    my_list = [1,2,3,55]
    for x in my_counter(my_list):
        print(x)


if __name__ == '__main__':
    main()