
def max_of_3_numb(a):
    if a[0] > a[1] and a[0] > a[2]:
        return a[0]
    elif a[1] > a[0] and a[1] > a[2]:
        return a[1]
    else:
        return a[2]
    print()

def sort(b):
    b.sort()
    print(b[-1])

def maxx(c):
    max(c)
    print(max(c))

if __name__ == "__main__":

    a = [23, 204, 106]
    print(max_of_3_numb(a))

    b = [32, 408, 34]
    print(sort(b))

    c = [67, 78, 59]
    print(maxx(c))




