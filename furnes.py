from data_frame import t, O, D

print(O)
print(D)
print(t)
import numpy as np

def furness (t ,O ,D , tol =1e-6 , maxit =1000):
    k =len( O )
    O = np . array ( O )[: , np . newaxis ]. astype (float)
    D = np . array ( D ). astype (float)
    t = np . array ( t )
    ai = np . ones (( k ,1))
    bj = np . ones ((1 , k ))
    iters =0
    while iters < maxit and np .max(abs( t .sum(1)/ O . transpose () - np . ones ((1 , k )))) > tol :
        ai = O /( t .sum(1)[: , np . newaxis ])
        t = t * np . dot ( ai , np . ones ((1 , k )))
        bj = D / t .sum(0)
        t = t * np . dot ( np . ones (( k ,1)) , bj [ np . newaxis ,:])
        iters +=1
    return t
