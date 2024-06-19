#function: generate instruction dictionary
#input : mods--logic gate library
#output : ins -- instruction library
# by O.L. , Jun 25,2016

def instr(mods):
    alpha='TCT'
    gamma='TAC'
    cal='CA' #close to alpha
    cg='TC'  #close to gamma
    ins=dict()
    l=len(mods)
    for i in range(l):
        #print (mods[i].typ)
        if mods[i].typ=='and':
            #print(mods[i].inp)
            key='INP(%d,%d)' %(mods[i].num,0)
            cin=mods[i].inp[0]
            v1=cal+alpha+cal+cin[0]+cg+gamma+cg
            v2=cal+alpha+cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value
            key='INP(%d,%d)' %(mods[i].num,1)
            cin=mods[i].inp[1]
            v1=cal+alpha+cal+cin[0]+cg+gamma+cg
            v2=cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value

        if mods[i].typ=='or':
            #print(mods[i].inp)
            key='INP(%d,%d)' %(mods[i].num,0)
            cin=mods[i].inp[0]
            v1=cal+alpha+cal+cin[0]+cg+gamma+cg
            v2=cal+alpha+cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value
            key='INP(%d,%d)' %(mods[i].num,1)
            cin=mods[i].inp[1]
            v1=cal+cin[0]+cg+gamma+cg
            v2=cal+alpha+cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value

        if mods[i].typ=='xor':
            #print(mods[i].inp)
            key='INP(%d,%d)' %(mods[i].num,0)
            cin=mods[i].inp[0]
            v1=cal+alpha+cal+cin[0]+cg+gamma+cg
            v2=cal+alpha+cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value
            key='INP(%d,%d)' %(mods[i].num,1)
            cin=mods[i].inp[1]
            v1=cal+cin[0]+cg+gamma+cg
            v2=cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value

        if mods[i].typ=='not':
            #print(mods[i].inp)
            key='INP(%d,%d)' %(mods[i].num,0)
            cin=mods[i].inp[0]
            v1=cal+alpha+cal+cin[0]+cg+gamma+cg
            v2=cal+alpha+cal+cin[1]+cg+gamma+cg
            value=[v1,v2]
            ins[key]=value
    for i in range(l):
        for j in range(l):
            if i !=j:
                key='WIR1(%d,%d,0)'%(mods[i].num,mods[j].num)
                value='adp1(%d,%d,0)'%(mods[i].num,mods[j].num)
                ins[key]=value
                if mods[j].typ !='not':
                    key='WIR1(%d,%d,1)'%(mods[i].num,mods[j].num)
                    value='adp1(%d,%d,1)'%(mods[i].num,mods[j].num)
                    ins[key]=value
    for i in range(l):
        for j in range(4):
            if i !=j:
                key='WIR2(%d,%d,0)'%(mods[i].num,mods[j].num)
                value='adp2(%d,%d,0)'%(mods[i].num,mods[j].num)
                ins[key]=value
    return ins
        
