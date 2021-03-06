from math import erf, sqrt

if __name__ == '__main__':
    mean, stdt_dev = list(map(int, input().split()))
    num = int(input())
    num2 = int(input())

    CDF = lambda x: 1/2 * (1 + erf((x - mean)/(stdt_dev * sqrt(2))))

    print(round(100 - CDF(num) * 100, 2), round(100 - CDF(num2) * 100, 2), round(CDF(num2) * 100, 2), sep = '\n')

