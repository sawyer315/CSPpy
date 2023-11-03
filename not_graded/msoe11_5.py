def f(x):
  return (-0.09 * (x ** 6)) + (1.6108 * (x ** 5)) + (-10.9167 * (x ** 4)) + (34.7625 * 
                                (x ** 3)) + (-54.0433 * (x ** 2)) + (31.1767 * x) - 4
def fp(x):
  return ((6*-0.09)*(x**5))+((5*1.6108)*(x**4))+((4*-10.0167)*(x**3))+((3*34.7625)+(x**2
                                                                                   ))+((2*-54.0433)*x)+31.1767
guess = float(input("Guess: "))
while abs(f(guess)) > 0.001:
  y = f(guess)
  print(f"f({guess}) = {y}")
  newGuess = guess - (f(guess)/fp(guess))
  guess = newGuess