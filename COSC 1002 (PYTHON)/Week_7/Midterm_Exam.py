def q1(f):
      return f*336
def q3(n):
      val = 0
      for i in range(1,n+1):
            val += i**3
      return val
def q5(n):
      for i in range(1,n+1):
            if (i%3==0) & (i%11==0):
                  print("foobar", end=" ")
            elif i%3==0:
                  print("foo", end=" ")
            elif i%11==0:
                  print("bar", end=" ")
            else:
                  print (i, end=" ")

def q6(string):
      val = ""
      for l in string:
            if l in "aeiouyAEIOUY":
                  val += "0"
            else:
                  val += l
      return val
