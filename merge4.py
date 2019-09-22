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
def mergesort(a,p,r):
    if r-p>=3:
        
        q1=p+(r-p)//4
        q2=p+2*(r-p)//4
        q3=p+(3*(r-p))//4
        mergesort(a,p,q1)
        mergesort(a,q1+1,q2)
        mergesort(a,q2+1,q3)
        mergesort(a,q3+1,r)
        merge4(a,p,q1,q2,q3,r)
    elif r-p<3:
        for t in range(p,r):
            if a[p]>a[r]:
                a[p],a[r]=a[r],a[p]
            if a[p]>a[t+1]:
                a[p],a[t+1]=a[t+1],a[p]
            if a[t+1]>a[r]:
                a[r],a[t+1]=a[t+1],a[r]
                
def merge4(A,p,q1,q2,q3,r):
    global number_comparisons
    n1=q1+1-p
    n2=q2-q1
    n3=q3-q2
    n4=r-q3
    L1,L2=[0]*n1,[0]*n2
    R1,R2=[0]*n3,[0]*n4
    L1=[A[p+i] for i in range(n1)]
    L1.append(1000000)
    L2=[A[q1+1+j] for j in range(n2)]
    L2.append(1000000)
    R1=[A[q2+1+k] for k in range(n3)]
    R1.append(1000000)
    R2=[A[q3+1+l] for l in range(n4)]
    R2.append(1000000)
    i,j,k,l=0,0,0,0
    for x in range(p,r+1):
        number_comparisons+=3
        if L1[i]<L2[j] and L1[i]<R1[k] and L1[i]<R2[l]:
            A[x]=L1[i]
            i+=1
        elif L2[j]<R1[k] and L2[j]<R2[l]:
            A[x]=L2[j]
            j+=1
        elif R1[k]<R2[l]:
            A[x]=R1[k]
            k+=1
        else:
            A[x]=R2[l]
            l+=1
            
number_comparisons=0
myarray=get_array()
x=time.time()
mergesort(myarray,0,len(myarray)-1)
print(str(len(myarray))+ ", " + str(number_comparisons) + ", " + str(time.time() - x))