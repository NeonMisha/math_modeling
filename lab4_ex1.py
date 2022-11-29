def u(a):
    s = 0
    for i in a:
        print(i)
        s = s + i
    g = s / len(a)
    print(g)

a = [1, 2, 5, 8, 9]
u(a)  