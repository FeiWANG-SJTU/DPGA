#function: generate input sequences
#input: num, changeable domain sequence
# output: inpt object
import modules

def gen_inp(num, cdomain):
    alpha='TCT'
    gamma='TAC'
    cal='CA' #close to alpha
    cg='TC'  #close to gamma
    s1=cal+alpha+cal+cdomain[0]+cg+gamma+cg
    s2=cal+alpha+cal+cdomain[1]+cg+gamma+cg
    ninp=modules.inpt(num)
    ninp.seq=[s1,s2]
    return(ninp)
def gen_oup(num,cdomain):
    alpha='TCT'
    gamma='TAC'
    cal='CA' #close to alpha
    cg='TC'  #close to gamma
    s1=cal+alpha+cal+cdomain[0]+cg+gamma+cg
    s2=cal+alpha+cal+cdomain[1]+cg+gamma+cg
    noup=modules.outp(num)
    noup.seq=[s1,s2]
    return noup
