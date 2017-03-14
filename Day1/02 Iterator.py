def main():
    f = open("test.txt", "w")
    print(f is f.__iter__())
    f.write("hey\n")
    f.close()


if __name__ == '__main__':
    main()