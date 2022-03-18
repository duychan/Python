n = 3
x = n*[0]


def fine_print(x):
   tmp = ''
   for i in x:
      tmp += str(i)
   return tmp


def bin_gen(i):
   for j in range(0,3):
      x[i] = j
      if i == n-1:
         print(fine_print(x))
      else:
         bin_gen(i+1)

bin_gen(0)