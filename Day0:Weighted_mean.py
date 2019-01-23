if __name__ == '__main__':
    n = int(input())
    X = list(map(int, input().split()))
    W = list(map(int, input().split()))

    m = sum(X[i]*W[i] for i in range(n))/sum(W)
    print(round(m, 1))
