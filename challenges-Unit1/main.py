num = (int(input("Enter a number:")))


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


result = fact_rec(num)
print("factorial of", num, "is:", result)
