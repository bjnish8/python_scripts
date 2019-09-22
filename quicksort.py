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


def quicksort(A,start,end):
    if start<end:
        partition_point=partition(A,start,end)
        quicksort(A,start,partition_point-1)
        quicksort(A,partition_point+1,end)

def partition(A,start,end):
    global number_comparisons
    #setting up last element of the array as the pivot
    pivot=A[end]
    #setting the initial index
    i=start-1
    for j in range(start, end):
        number_comparisons+=1
        if A[j]<=pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[end]=A[end],A[i+1]
    return (i+1)

if __name__=="__main__":
    try:
    	Ax = [33,22,43,53,12,42,1,57,100,34]
    	A=get_array()
    	number_comparisons=0
    	x=time.time()
    	quicksort(A,0,len(A)-1)
    	print(str(len(A))+ ", " + str(number_comparisons) + ", " + str(time.time() - x))
    except RecursionError:
        print("Recursion Error for file " + str(sys.argv[1]) + ". Maximum recursion depth exceeded in comparison.")
    except:
        print("An error occurred.")
