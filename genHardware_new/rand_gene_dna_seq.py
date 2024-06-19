#randomly generate a DNA sequence
import numpy as np
import random
def rand_seq(n):
    a=[]
    
    i=0
    while i <n:
        rr=np.random.uniform()
        if rr<0.25:
            a.append('A')
        elif rr<0.5:
            a.append('T')
        elif rr<0.75:
            a.append('C')
        else :
            a.append('G')
        if i>1 and a[i]=='G'and a[i-1]=='G'and a[i-2]=='G':#DELETE GGG OR CCC
            a.pop()
            i=i-1
        if i>1 and a[i]=='C'and a[i-1]=='C'and a[i-2]=='C':
            a.pop()
            i=i-1
        if i>2 and a[i]=='A'and a[i-1]=='A'and a[i-2]=='A'and a[i-3]=='A':#DELETE AAAA OR TTTT
            a.pop()
            i=i-1
        if i>2 and a[i]=='T'and a[i-1]=='T'and a[i-2]=='T'and a[i-3]=='T':
            a.pop()
            i=i-1
        i=i+1
    return a
    
    
##a=rand_seq(20);
##print (''.join(a))
