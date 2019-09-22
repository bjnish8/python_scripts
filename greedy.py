
# coding: utf-8

# In[22]:

from sys import argv
import time
def greedy(v,a,d):
    d  = sorted(d, reverse=True)
    coins = []
    for i in d:
        while v>=i:
            v-=i
            coins.append(i)
    return(coins)
    


# In[24]:


coins = list(map(int, argv[3].strip('[]').split(',')))
x = time.time()
selected_coins = greedy(int(argv[1]),int(argv[2]),coins)
print(selected_coins, time.time()-x)

