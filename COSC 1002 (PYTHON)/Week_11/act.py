def quiz(*args):
      total = 1
      for val in args:
            total *= val
      return total ** (1/len(args))

