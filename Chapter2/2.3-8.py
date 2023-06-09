# S - A set of n integers
# x - An integer (we'll call it "target")
# Goal -> Find some integers a,b in S, s.t x = a+b


# Returns index OR -1 if element is not found
def BinarySearch(A, target, l, r):
  if r >= l:
    # Calculating the midpoint incorrectly 

    mid = l + ((r-l) // 2)

    # print("A", A)
    print("A", A)
    print("target", target)
    print("mid", mid)
    print("l", l)
    print("r", r)

    if A[mid] == target:
      return mid
    elif A[mid] < target:
      return BinarySearch(A, target, mid+1, r)
    else:
      return BinarySearch(A, target, l, mid-1)
  else:
    return -1
  
def FindSumOfTarget(arr, target):    
  # Pretend this is mergeSort for now
  arr.sort()
  print(arr)
  
  for i, val in enumerate(arr):
    temp = target - val
    res = BinarySearch(arr, temp, 0, len(arr)-1)

    print("temp:", temp)
    print("res: ", res)
    
    if res != -1:
      return True

  return False



test = [1,8,2,7,3,6,4,5,4,6,3,1,2]
target = 50
final = FindSumOfTarget(test, target)

print("Final", final)

# Implement later
# def Merge():
# def MergeSort():