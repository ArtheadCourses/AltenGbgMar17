import timeit

def main():
    result = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    print(result)

if __name__ == '__main__':
    main()