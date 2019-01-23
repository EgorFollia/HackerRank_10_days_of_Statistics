from collections import Counter

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))

    mean = sum(x)/n

    x = sorted(x)
    if (len(x) % 2 == 0):
        median = (x[n // 2 - 1] + x[n // 2])/2
    else:
        median = x[len(x)//2]

    mode = sorted(sorted(Counter(x).items()), key = lambda mod: mod[1], reverse = True)[0][0]

    print(mean, median, mode, sep = '\n')

'''
or you can use scipy and numpy
np.mean(x)
np.median(x)
scipy.stats.mode(x)
'''
