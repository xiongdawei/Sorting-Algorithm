
def quick_sort(alist,first,last):
  pivot = first
  leftmark = 1
  rightmark = last
  boolean = False
  #print(alist[pivot])
  #print(alist[leftmark])
  #print(alist[rightmark])
  while not boolean:

    if leftmark<=rightmark:
      if alist[leftmark] <= alist[pivot]:
        leftmark+=1
       #print("leftmark",leftmark,"rightmark",rightmark)


      elif alist[rightmark] >= alist[pivot]:
        rightmark-=1
        #print("leftmark",leftmark,"rightmark",rightmark)

      else:
        alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
        #print("leftmark",leftmark,"rightmark",rightmark)

    else:
      boolean = True

  alist[pivot],alist[rightmark] = alist[rightmark], alist[pivot]
  return rightmark

def quicksort(alist):
  quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):
  if first<last:
    splitpoint = quick_sort(alist,first,last)
    quicksorthelper(alist,first,splitpoint-1)
    quicksorthelper(alist,splitpoint+1,last)

def selectionsort(x):
    a = []
    while len(x)!=0:
        minn = x[0]
        for i in range(len(x)):
            if x[i]<minn:
                minn = x[i]
        a.append(minn)
        x.remove(minn)
    return a
  
  
def merge(left,right):
    result = []
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):
    if len(L)<2:
        return L[:]
    else:
        mid = int(len(L)/2)
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left,right)
      
def insertionsort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            
            i-=1
        A[i+1] = key
    return A
  
  
def bubblesort(a):
    length = len(a)
    while length>0:
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                
        length-=1
    return a
 

  
a = [109,34,22,202,5,1,6,56,23,12,67,40,9,23,54]
quicksort(a)
print(a)
