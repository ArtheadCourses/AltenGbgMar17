import time

def main():

    original = list(open('alice.txt','r'))
    original = original * 10
    print(len(original))
    all_lines = ""
    start = time.time()
    for line in original:
        all_lines += line
    end = time.time()
    print(end-start, "seconds")

    start = time.time()
    all_lines2 = "".join(original)
    end = time.time()
    print(end-start, "seconds")

    print(all_lines == all_lines2)
    print(all_lines is all_lines2)

    o = ['ABC']
    o = o * 10
    print(o)
    r = "".join(o)
    print(r)

if __name__ == '__main__':
    main()