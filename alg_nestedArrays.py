def main():
    a = [1, 2, 3] #6
    b = [1, [2], 3] #6
    c = [[[[[[5]]]]]] #5
    d = [10, [12, 14, [1], [16, [20]]], 10, 11] #94

    print(nestedAdd(a))
    print(nestedAdd(b))
    print(nestedAdd(c))
    print(nestedAdd(d))


def nestedAdd(array):
    total = 0

    for i in range(len(array)):
        current = array[i]
        if type(current) == list:
            total += nestedAdd(current)
        else:
            total += current

    return total


if __name__ == "__main__":
    main()