def BubbleSort(A):
  for i in range(0, len(A)-1):
    for j in range(0, len(A)-1):
      if A[j] > A[j+1]:
        temp = A[j]
        A[j] = A[j+1]
        A[j+1] = temp

def SelectionSort(A):
  for i in range(0, len(A)-1):
    minIndex = i
    for j in range(i+1, len(A)-1):
      if A[j] < A[minIndex]:
        minIndex = j
    temp = A[i]
    A[i] = A[minIndex]
    A[minIndex] = temp

def InsertionSort(A):
  for i in range(1, len(A)):
    key = A[i]
    j = i-1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key