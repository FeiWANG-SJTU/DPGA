# in this program, an and gate has 3 strands
#function : generate a logic gate
# input: logic type, changeable domain sequence
# output : the sequences of generated logic gate
# by O.L, Mar 18 ,2016

import rev_comp_of_seq as rec
import modules

def gen_lgat(typ,num,cdomain):
    alpha='TCT'
    gamma='TAC'
    cal='CA' #close to alpha
    cg='TC'  #close to gamma
    
    if typ==1: #and gate
        rs1=cal+alpha+cal+cdomain[0]+cg+gamma+cg #in=0
        s1=rec.rev_comp(rs1)
        s2= cg+cdomain[1]+cal+alpha+cal+cdomain[0]+cg #o=0
        rs3=cal+alpha+cal+cdomain[2]+cg+gamma+cg+cal+cdomain[3]+cg+gamma+cg
        s3=rec.rev_comp(rs3)  #in=1
        s4=cg+cdomain[4]+cal+alpha+cal+cdomain[2]+cg #o=1
        s5=gamma[1:3]+cg+cal+cdomain[3]+cg
        in0=[cdomain[0],cdomain[2]]
        in1=[cdomain[0],cdomain[3]]
        out=[cdomain[1],cdomain[4]]
        genG=modules.modul(num)
        genG.num=num
        genG.typ='and'
        genG.inp.append(in0)
        genG.inp.append(in1)
        genG.out=out
        genG.gate_seq.append(s1)
        genG.gate_seq.append(s2)
        genG.gate_seq.append(s3)
        genG.gate_seq.append(s4)
        genG.gate_seq.append(s5)
        return genG
    elif typ==2: # or gate
        rs3=cal+alpha+cal+cdomain[0]+cg+gamma+cg #in=1
        s3=rec.rev_comp(rs3)
        s4= cg+cdomain[1]+cal+alpha+cal+cdomain[0]+cg #o=1
        rs1=cal+alpha+cal+cdomain[2]+cg+gamma+cg+cal+cdomain[3]+cg+gamma+cg
        s1=rec.rev_comp(rs1)
        s2=cg+cdomain[4]+cal+alpha+cal+cdomain[2]+cg
        ss2=gamma[1:3]+cg+cal+cdomain[3]+cg
        in0=[cdomain[2],cdomain[0]]
        in1=[cdomain[3],cdomain[0]]
        out=[cdomain[4],cdomain[1]]
        genG=modules.modul(num)
        genG.num=num
        genG.typ='or'
        genG.inp.append(in0)
        genG.inp.append(in1)
        genG.out=out
        genG.gate_seq.append(s1)
        genG.gate_seq.append(s2)
        genG.gate_seq.append(s3)
        genG.gate_seq.append(s4)
        genG.gate_seq.append(ss2)
        return genG
    elif typ==3: # xor gate
        rs1=cal+alpha+cal+cdomain[0]+cg+gamma+cg+cal+cdomain[2]+cg+gamma+cg
        s1=rec.rev_comp(rs1)   #in1=0 in2=0
        s2=cg+cdomain[4]+cal+alpha+cal+cdomain[0]+cg
        ss2=gamma[1:3]+cg+cal+cdomain[2]+cg
        rs3=cal+alpha+cal+cdomain[0]+cg+gamma+cg+cal+cdomain[3]+cg+gamma+cg
        s3=rec.rev_comp(rs3)    #in1=0 in2=1
        s4=cg+cdomain[5]+cal+alpha+cal+cdomain[0]+cg
        ss4=gamma[1:3]+cg+cal+cdomain[3]+cg
        rs5=cal+alpha+cal+cdomain[1]+cg+gamma+cg+cal+cdomain[2]+cg+gamma+cg
        s5=rec.rev_comp(rs5)   #in1=1 in2=0
        s6=cg+cdomain[5]+cal+alpha+cal+cdomain[1]+cg
        ss6=gamma[1:3]+cg+cal+cdomain[2]+cg
        rs7=cal+alpha+cal+cdomain[1]+cg+gamma+cg+cal+cdomain[3]+cg+gamma+cg
        s7=rec.rev_comp(rs7)  #in1=1 in2=1
        s8=cg+cdomain[4]+cal+alpha+cal+cdomain[1]+cg
        ss8=gamma[1:3]+cg+cal+cdomain[3]+cg
        in0=[cdomain[0],cdomain[1]]
        in1=[cdomain[2],cdomain[3]]
        out=[cdomain[4],cdomain[5]]
        genG=modules.modul(num)
        genG.num=num
        genG.typ='xor'
        genG.inp.append(in0)
        genG.inp.append(in1)
        genG.out=out
        genG.gate_seq.append(s1)
        genG.gate_seq.append(s2)
        genG.gate_seq.append(s3)
        genG.gate_seq.append(s4)
        genG.gate_seq.append(s5)
        genG.gate_seq.append(s6)
        genG.gate_seq.append(s7)
        genG.gate_seq.append(s8)
        genG.gate_seq.append(ss2)
        genG.gate_seq.append(ss4)
        genG.gate_seq.append(ss6)
        genG.gate_seq.append(ss8)
        return genG
        
        
    elif typ==4: # not gate
        rs3=cal+alpha+cal+cdomain[0]+cg+gamma+cg #in=0
        s3=rec.rev_comp(rs3)
        s4= cg+cdomain[3]+cal+alpha+cal+cdomain[0]+cg #o=1
        rs1=cal+alpha+cal+cdomain[1]+cg+gamma+cg #in=1
        s1=rec.rev_comp(rs1)
        s2= cg+cdomain[2]+cal+alpha+cal+cdomain[1]+cg #o=0
        in0=[cdomain[0],cdomain[1]]
        in1=[]
        out=[cdomain[2],cdomain[3]]
        genG=modules.modul(num)
        genG.num=num
        genG.typ='not'
        genG.inp.append(in0)
        genG.inp.append(in1)
        genG.out=out
        genG.gate_seq.append(s1)
        genG.gate_seq.append(s2)
        genG.gate_seq.append(s3)
        genG.gate_seq.append(s4)
        
        return genG
    else:
        print ('ERROR: NOT CONTAIN THIS TYPE!')
        return
    

