import time
import sys
def get_array():    
    with open(sys.argv[1]) as file: 
        array=[]
        for line in file: 
            line = line.strip('\n')
            array.append (line)
        for x in range(len(array)):
            array[x]=int(array[x])
        return array

def max_heapify(A, i): 
    global heap_size
    global number_comparisons
    l = 2 * i + 1
    r = 2 * i + 2
    number_comparisons+=1
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    number_comparisons+=1
    if r < heap_size and A[r] > A[largest]:
        largest = r
    number_comparisons+=1
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A, largest) 
        
def build_max_heap(A):
    for i in range((len(A)-1)//2, -1, -1): 
        max_heapify(A, i) 
  
def heapsort(A): 
    global heap_size
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1): 
        A[i], A[0] = A[0], A[i] 
        heap_size = heap_size-1
        max_heapify(A, 0) 
        
if __name__=="__main__":
    number_comparisons=0
    myarray=get_array()
    heap_size=len(myarray)
    x=time.time()
    heapsort(myarray)
    print(str(len(myarray))+ ", " + str(number_comparisons) + ", " + str(time.time() - x))