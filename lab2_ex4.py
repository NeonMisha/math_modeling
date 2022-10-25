a = int(input())
f1 = 1
f2 = 1
while a > 0:
  f3 = f1 + f2
  print(f3)
  f1 = f2
  f2 = f3
  a = a - 1
  