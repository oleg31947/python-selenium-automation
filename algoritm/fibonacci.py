def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


if __name__ == "__main__":
    print(fibonacci(2000))
