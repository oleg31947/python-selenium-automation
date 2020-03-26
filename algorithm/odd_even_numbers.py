

def even_and_odd(x):
    odd_counter = 0
    even_counter = 0
    for i in str(x):
        if int(i) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    print(f'Odd numbers are {odd_counter}, and Even numbers are {even_counter}.')


if __name__ == "__main__":
    print(even_and_odd(5476291))


