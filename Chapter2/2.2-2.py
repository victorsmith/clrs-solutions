
def selectionSort(arr, n):
  A = arr
  ptr = 0
  print(A)    
  # for i in range(1, n-1)
  for ptr in range(0,n):
    print("--------------  ptr: ", ptr+1)
    
    # Default value
    smallest = ptr
    for i in range(ptr, n):
      if A[smallest] > A[i]:
        # Swap the values
        smallest = i

    # Swap values
    A[ptr], A[smallest] = A[smallest], A[ptr]

    ptr += 1
    print(A)    


testA1 = [1, 6, 3, 1, 2, 11, -3]
selectionSort(testA1, len(testA1))

# 