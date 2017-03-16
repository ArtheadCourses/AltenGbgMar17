from collections import deque



def countdown(n):
    while n > 0:
        yield n
        n -= 1


def run(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task Done")


def main():
    tasks = deque()
    tasks.extend([countdown(10), countdown(4), countdown(6)])
    run(tasks)


if __name__ == '__main__':
    main()