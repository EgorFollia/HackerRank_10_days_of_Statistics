if __name__ == '__main__':
    n, d = input().split()
    ins = int(input())
    p = int(n)/int(d)

    print(round(sum([((1 - p) ** (ins - 1)) * p for ins in range(1, ins + 1)]), 3))

