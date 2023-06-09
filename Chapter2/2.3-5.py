
# A recursive algoritm is still the same algorithm. The fundamentals of what we're doing don't change
def recursiveInsertionSort(A, n):
  if n < 2:
    return
  

  print(A[:n])
  recursiveInsertionSort(A, n-1)
  
  key = A[n-1]
  print("key", key)

  i = n-2
  print("i", i)

  while i >= 0 and A[i] < key:
    A[i+1] = A[i]
    i -= 1

  A[i+1] = key

  print("A: ",A)
  
  

test = [3, 1, 2, 8]
length = len(test)
recursiveInsertionSort(test, length)

