if __name__ == '__main__':
    n, d = input().split()
    ins = int(input())
    p = int(n)/int(d)

    print(round(((1 - p) ** (ins - 1)) * p, 3))


