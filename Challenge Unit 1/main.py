def fact(n):
  if (n == 0):
    return 1
  else:
    return n * fact(n - 1)

def main():
  inp = int(input("Enter a number to calculate factorial : "))
  out = fact(inp)
  print("Factorial of the given number : ", out)
main()
