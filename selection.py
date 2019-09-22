import time
import sys
def get_array():    
    with open("data.txt") as file: 
        array = [line.strip('\n') for line in file]
        for x in range(len(array)):
            array[x]=int(array[x])
        return array

def selection_sort(A): 
    number_comparisons = 0
    x=time.time()
    n=len(A)
    for i in range(n-1):
        smallest=i
        for j in range(i+1,n):
            number_comparisons+=1
            if A[j]<A[smallest]:
                
                smallest=j
        # swap A[i] with smallest number
        A[smallest],A[i]=A[i],A[smallest]
    
    print(str(len(A))+ ", " + str(number_comparisons) + ", " + str(time.time() - x))


print("hello")
myarray=get_array()
selection_sort(myarray)



