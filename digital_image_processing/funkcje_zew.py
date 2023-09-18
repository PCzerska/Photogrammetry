import numpy as np

def usuwanie(punkciki):
    wyniki = []
    for punkt in punkciki:
        podobny = False
        x, y = punkt
        for istniejacy in wyniki:
            ist_x, ist_y = istniejacy
            if abs(x - ist_x) <= 100 and abs(y - ist_y) <= 100:
                podobny = True
                break
        if not podobny:
            wyniki.append(punkt)
    return wyniki

def transform(file, punkciki):
    A=[]
    dane = np.genfromtxt(file, delimiter='\t')
    dane = dane[:,1:]
    L = dane[:,:].reshape(-1)
    for ev in punkciki:
        x = ev[0]
        y = ev[1]
        A.append([1,x,y,0,0,0])
        A.append([0,0,0,1,x,y])
    A = np.array(A)
    Xn = np.linalg.inv(np.transpose(A)@A)@np.transpose(A)@L
    return L,A,Xn






