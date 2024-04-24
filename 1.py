import numpy as np

def derivasjon(h):
    F = (np.exp(1.5+h)-np.exp(1.5))/h
    return F

for i in range(17):
    a= 0.1**i
    print(derivasjon(a), a)