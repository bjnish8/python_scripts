def bottom(value, deno):
    data = {x: list() for x in range(value + 1)}
    
    for i in range(1, value+1):
        mini = 100000
        for j in deno:
            if i >= j:
                if mini > len(data[i - j]) + 1:
                    mini = len(data[i - j]) + 1    
                    temp = j
        data[i].append(temp)
        data[i].extend(data[i-temp])
    for i, j in data.items():
        print(i, j, end='\n')
    return len(data[value])
    
    
print(bottom(63, [1, 5, 10, 21, 25]))
    

print([0 for x in range(8)])