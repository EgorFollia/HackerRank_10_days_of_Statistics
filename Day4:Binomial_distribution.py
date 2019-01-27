from math import factorial

if __name__ == '__main__':
    p, n = 1.09/2.09, 6

    bin_dist = sum([(factorial(n)/(factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x)) for x in range(3, 7)])
    
    print(round(bin_dist, 3))


