def fibonacci_recursion(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci(n):
  if n <= 0:
        return 0
  elif n == 1:
        return 1
    
  a, b = 0, 1
  for _ in range(2, n + 1):
        a, b = b, a + b
  return b

if __name__ == "__main__":
  Exit = True
  while Exit:
    print("1) Using recursion")
    print("2) Using without recursion")
    print("3) Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
      Number = int(input("Enter number of fibonacci series : "))
      print(Number, "th Fibonacci number is : ", fibonacci_recursion(Number))
    if choice == 2:
      Number = int(input("Enter number of fibonacci series : "))
      print(Number, "th Fibonacci number is : ", fibonacci(Number))
    if choice == 3:
      Exit = False