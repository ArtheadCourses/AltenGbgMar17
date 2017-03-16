
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)

def main():
    search = grep('hello')
    next(search)

    search.send('hi there')
    search.send('hello there')
    search.send('bye bye')


if __name__ == '__main__':
    main()