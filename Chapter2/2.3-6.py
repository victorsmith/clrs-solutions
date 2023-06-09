# Binary Search 

def BinarySearch(A, target, l, r):

    # base case 
    if r >= l:

      mid = len(A) // 2
      if A[mid] == target:
        return mid
      elif A[mid] > target:
        # must return here to pass up the result from deeper in the recursion
        return BinarySearch(A, target, l, mid-1)
      else:
        # must return here to pass up the result from deeper in the recursion
        return BinarySearch(A, target, mid+1, r)
    else:
      return -1
    
        
    print("binarySearch", A)

test = [1, 2, 4, 5, 6, 7, 7, 9, 11, 23]
BinarySearch(test, 2, 0, len(test)-1)
