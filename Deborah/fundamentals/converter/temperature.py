def C2K(C):
    assert (C > -273.15)
    return C + 273.15

def K2C(K):
    assert (K>0)
    return K - 273.15

def F2C(F):
    assert (F > -459.67)
    return (F-32)/1.8
