a = int(input())
b = int(input())
if b == 0:
  print("это ноль")
elif a % b == 0:
  print("оно делиться без остатка ТЫ МОЛОДЕЦ!!!!")
  print(a/b)
else:
  g = a % b
  print("оно не делиться без остатка ТЫ НЕ МОЛОДЕЦ!!!! остаток:")
  print(g)
  print(a/b)