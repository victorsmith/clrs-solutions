def AddBinaryInteger(A, B):
  C = [0 for x in range(len(A)+1)]
  carry = 0

  for i in range(len(A)-1, -1, -1):
      res = A[i] + B[i] + carry      
      
      if res == 3:
        C[i+1] = 1
        carry = 1
      elif res == 2:  
        C[i+1] = 0
        carry = 1
      elif res == 1:
        C[i+1] = 1
        carry = 0
      elif res == 0:
        C[i+1] = 0
        carry = 0
  C[len(A)] = carry
  return C

#  4 3 2 1 0
A=[0,1,1,1,1]
B=[0,1,1,1,1]
 
print("A[0]", A[0])
print("B[0]", B[0])

AddBinaryInteger(A,B)