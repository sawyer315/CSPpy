num = int(input("n = ? "))
def isprime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i ** 2 <= n:
    if n % i == 0:
      return False
    i += 2
  return True
answer = isprime(num)
print(answer)