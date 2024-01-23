class Mergesort:
  @staticmethod
  def sort(A):
    if len(A) > 1:
      middle = round(len(A)/2)
      L = A[0:middle]
      R = A[middle:]
      Mergesort.sort(L)
      Mergesort.sort(R)
      Mergesort.merge(A, L, R)
    return(A)
  @staticmethod
  def merge(A, L, R):
    j=0
    i=0
    k=0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        A[k] = L[i]
        i +=1
      else:
        A[k] = R[j]
        j +=1
      k +=1
    while i < len(L):
      A[k] = L[i]
      i +=1
      k +=1
    while j < len(R):
      A[k] = R[j]
      j +=1
      k +=1
list = [4,2,5,3,1]
Mergesort.sort(list)
print(list)