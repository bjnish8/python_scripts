from sys import argv
import time
def changemake(v,a,d):
    if v in d:
        return 1
    q=10000
    for i in range(a):
        if v>d[i]:
            q = min (q, 1 + changemake(v-d[i],a,d))
    return q


coins = list(map(int, argv[3].strip('[]').split(',')))
x = time.time()
number_of_coins = changemake(int(argv[1]),int(argv[2]),coins)
print(number_of_coins, time.time()-x)

