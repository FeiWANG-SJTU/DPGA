# function:
# generate threshold circuit corresponding to output of each logic gate
# input: a gate library
# output: a threshold library
# by O.L. Jun 25, 2016

import rev_comp_of_seq as rec

def gen_th(mods):
    alpha='TCT'
    gamma='TAC'
    cal='CA'
    cg='TC'

    th_lib=[]

    for mod in mods:
        cout=mod.out
        print (cout)
        t1=rec.rev_comp(cg+cout[0]+cal+alpha+cal)
        t2=cg+cout[0]
        t3=rec.rev_comp(cg+cout[1]+cal+alpha+cal)
        t4=cg+cout[1]
        th=[t1,t2,t3,t4]
        th_lib.append(th)
    return th_lib
