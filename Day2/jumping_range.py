
def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

def main():
    iterable = jumping_range(12)

    for value in iterable:
        print(value)
        if value == 4:
            iterable.send(2)


if __name__ == '__main__':
    main()