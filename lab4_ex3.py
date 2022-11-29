G = 9.8

def u(m, h, V):
    Ek = m*V**2/2
    Ep = m*G*h
    Em = Ek + Ep
    print(Em)
    
u(2, 6, 8)