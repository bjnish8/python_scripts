def rodcut(price, n):
    revenue = [-1] * (n + 1)
    revenue[0] = 0
    optimum = [0]
    for i in range(1, n + 1):
        maxi = -1
        for j in range(1, i + 1):
            temp = price[j-1] + revenue[i - j]
            if maxi < temp:
                maxi = temp
                xx = j
        optimum.append(xx)    
        revenue[i] = maxi
    return revenue[n], optimum[n]

x = ([rodcut([1, 5, 8, 9 ,10],n) for n in range(1, 6)])
print(x)