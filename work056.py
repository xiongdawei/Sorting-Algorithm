
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



  
a = [109,34,22,202,5,1,6,56,23,12,67,40,9,23,54]
quicksort(a)
print(a)
