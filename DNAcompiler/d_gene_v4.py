# function: generate machine code version 4
# generate Instructions from Intermediate code
# by OL , Aug 24, 2021
import re
import math
from d_inte_gene_2bit_bus import incd
#import simple_operations as sop
global poin
poin={'or':1000,'and':1006,'not':1012,'xor':1018}

def adder(inp1,inp2,oup):
    #2bit inp1[0] inp1[1] inp2[0] inp2[1]
    # out: oup[0] oup[1]
    global poin 
    tmp_table=[]
    # compiling of 1bit full adder
    if poin['xor']>1021 or poin['and']>1010: # pointer for and xor
        #print(poin['xor'],poin['and'])
        print( 'ERROR: SPACE not enough')
        return -1
    else :
        addr=[['id',poin['xor']],oup[0]]
        tmp_table.append([addr,[inp1[0],inp2[0]],oup[0]])
        poin['xor']+=1
        addr=[['id',poin['and']],poin['xor']+1]
        tmp_table.append([addr,[inp1[0],inp2[0]],poin['xor']+1])
        poin['and']+=1
        addr=[['id',poin['xor']],poin['xor']+1]
        tmp_table.append([addr,[inp1[1],inp2[1]],poin['xor']+1])
        poin['xor']+=1
        addr=[['id',poin['xor']],oup[1]]
        tmp_table.append([addr,[['id',poin['xor']-1],['id',poin['and']-1]],oup[1]])
        poin['xor']+=1
##        for tmp in tmp_table:
##            print(tmp)
        return tmp_table
def sub(inp1,inp2,oup):
    # 2bit data
    global poin
    tmp_table=[]
    if poin['or']>1006 or poin['and']>1010 or poin['not']>1016 or poin['xor']>1022:
        print('ERROR: Space Not Enough!!!')
        return -1
    else:
        addr=[['id',poin['and']],poin['and']+1]
        tmp_table.append([addr,[inp1[1],['id',poin['not']]],poin['and']+1])
        poin['and']+=1
        addr=[['id',poin['not']],poin['and']-1]
        tmp_table.append([addr,[inp2[1]],poin['and']-1])
        poin['not']+=1
        addr=[['id',poin['not']],poin['or']]
        tmp_table.append([addr,[inp2[0]],poin['or']])
        poin['not']+=1
        addr=[['id',poin['or']],poin['and']]
        tmp_table.append([addr,[inp1[0],['id',poin['not']-1]],poin['and']])
        poin['or']+=1
        addr=[['id',poin['xor']],oup[0]]
        tmp_table.append([addr,[inp1[0],inp2[0]],oup[0]])
        poin['xor']+=1
        addr=[['id',poin['and']],oup[1]]
        tmp_table.append([addr,[['id',poin['and']-1],['id',poin['or']-1]],oup[1]])
        poin['and']+=1
        return tmp_table 

def mul(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['and']>1009 or poin['xor']>1023:
        print('ERROR: Space Not Enough!!!')
        return -1
    else:
        addr=[['id',poin['and']],oup[0]]
        tmp_table.append([addr,[inp1[0],inp2[0]],oup[0]])
        poin['and']+=1
        addr=[['id',poin['and']],poin['xor']]
        tmp_table.append([addr,[inp1[1],inp2[0]],poin['xor']])
        poin['and']+=1
        addr=[['id',poin['and']],poin['xor']]
        tmp_table.append([addr,[inp1[0],inp2[1]],poin['xor']])
        poin['and']+=1
        addr=[['id',poin['xor']],oup[1]]
        tmp_table.append([addr,[['id',poin['and']-2],['id',poin['and']-1]],oup[1]])
        poin['xor']+=1
        return tmp_table
def div(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['and']>1008 or poin['or']>1005 or poin['not']>1016:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['not']],poin['and']+1]
        tmp_table.append([addr,[inp2[1]],['id',poin['and']+1]])
        poin['not']+=1
        addr=[['id',poin['not']],poin['and']]
        tmp_table.append([addr,[inp2[0]],['id',poin['and']]])
        poin['not']+=1
        addr=[['id',poin['and']],poin['or']+1]
        tmp_table.append([addr,[inp2[1],['id',poin['not']-1]],poin['or']+1])
        poin['and']+=1
        addr=[['id',poin['and']],[poin['or'],poin['and']+1]]
        tmp_table.append([addr,[['id',poin['not']-2],inp2[0]],[poin['or'],poin['and']+1]])
        poin['and']+=1
        addr=[['id',poin['or']],poin['and']+2]
        tmp_table.append([addr,[inp1[1],['id',poin['and']-1]],poin['and']+2])
        poin['or']+=1
        addr=[['id',poin['or']],poin['and']+1]
        tmp_table.append([addr,[inp1[0],['id',poin['and']-2]],poin['and']+1])
        poin['or']+=1
        addr=[['id',poin['and']],oup[1]]
        tmp_table.append([addr,[inp1[1],['id',poin['and']-1]],oup[1]])
        poin['and']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[inp1[1],['id',poin['or']-1]],poin['or']])
        poin['and']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[['id',poin['or']-2],inp1[0]],poin['or']])
        poin['and']+=1
        addr=[['id',poin['or']],oup[0]]
        tmp_table.append([addr,[['id',poin['and']-2],['id',poin['and']-1]],oup[0]])
        poin['or']+=1
        return tmp_table
def dand(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['and']>1011 or poin['or']>1004:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['and']]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['and']]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['and']]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['and']]])
        poin['or']+=1
        addr=[['id',poin['and']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],oup[0]])
        poin['and']+=1
        return tmp_table
def dor(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['or']>1003:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['or']+2]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['or']+2]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['or']+1]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['or']+1]])
        poin['or']+=1
        addr=[['id',poin['or']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],oup[0]])
        poin['or']+=1
        return tmp_table
def dxor(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['or']>1004 or poin['xor']>1023:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['xor']]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['xor']]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['xor']]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['xor']]])
        poin['or']+=1
        addr=[['id',poin['xor']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],oup[0]])
        poin['xor']+=1
        return tmp_table
def dnot(inp1,oup):
    global poin
    tmp_table=[]
    if poin['or']>1005 or poin['not']>1017:
        print("ERROR: Space Not Enough.")
        return -1
    else:
        addr=[['id',poin['or']],poin['not']]
        tmp_table.append([addr,[inp1[0],inp1[1]],['id',poin['not']]])
        poin['or']+=1
        addr=[['id',poin['not']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-1]],oup[0]])
        poin['not']+=1
        return tmp_table
def dxnor(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['xor']>1023 or poin['or']>1004 or poin['not']>1017:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['xor']]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['xor']]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['xor']]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['xor']]])
        poin['or']+=1
        addr=[['id',poin['xor']],['id',poin['not']]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],['id',poin['not']]])
        poin['xor']+=1
        addr=[['id',poin['not']],oup[0]]
        tmp_table.append([addr,[['id',poin['xor']-1]],oup[0]])
        poin['not']+=1
        return tmp_table
def dnor(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['or']>1003 or poin['not']>1017:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['or']+2]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['or']+2]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['or']+1]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['or']+1]])
        poin['or']+=1
        addr=[['id',poin['or']],['id',poin['not']]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],['id',poin['not']]])
        poin['or']+=1
        addr=[['id',poin['not']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-1]],oup[0]])
        poin['not']+=1
        return tmp_table
def dnand(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['or']>1004 or poin['not']>1017 or poin['and']>1011:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['or']],poin['and']]
        tmp_table.append([addr,[inp1[1],inp1[0]],['id',poin['and']]])
        poin['or']+=1
        addr=[['id',poin['or']],poin['and']]
        tmp_table.append([addr,[inp2[1],inp2[0]],['id',poin['and']]])
        poin['or']+=1
        addr=[['id',poin['and']],['id',poin['not']]]
        tmp_table.append([addr,[['id',poin['or']-2],['id',poin['or']-1]],['id',poin['not']]])
        poin['and']+=1
        addr=[['id',poin['not']],oup[0]]
        tmp_table.append([addr,[['id',poin['and']-1]],oup[0]])
        poin['not']+=1
        return tmp_table
def eq(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['xor']>1022 or poin['or']>1005 or poin['not']>1017:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['xor']],poin['or']]
        tmp_table.append([addr,[inp1[1],inp2[1]],['id',poin['or']]])
        poin['xor']+=1
        addr=[['id',poin['xor']],poin['or']]
        tmp_table.append([addr,[inp1[0],inp2[0]],['id',poin['or']]])
        poin['xor']+=1
        addr=[['id',poin['or']],poin['not']]
        tmp_table.append([addr,[['id',poin['xor']-2],['id',poin['xor']-1]],['id',poin['not']]])
        poin['or']+=1
        addr=[['id',poin['not']],oup[0]]
        tmp_table.append([addr,[['id',poin['or']-1]],oup[0]])
        poin['not']+=1
        return tmp_table
def neq(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['xor']>1022 or poin['or']>1005:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['xor']],poin['or']]
        tmp_table.append([addr,[inp1[1],inp2[1]],['id',poin['or']]])
        poin['xor']+=1
        addr=[['id',poin['xor']],poin['or']]
        tmp_table.append([addr,[inp1[0],inp2[0]],['id',poin['or']]])
        poin['xor']+=1
        addr=[['id',poin['or']],oup[0]]
        tmp_table.append([addr,[['id',poin['xor']-2],['id',poin['xor']-1]],oup[0]])
        poin['or']+=1
        return tmp_table
def lthan(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['not']>1015 or poin['or']>1005 or poin['and']>1009 or poin['xor']>1023:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['not']],poin['and']]
        tmp_table.append([addr,[inp2[1]],['id',poin['and']]])
        poin['not']+=1
        addr=[['id',poin['not']],poin['and']+1]
        tmp_table.append([addr,[inp2[0]],['id',poin['and']+1]])
        poin['not']+=1
        addr=[['id',poin['not']],poin['and']+2]
        tmp_table.append([addr,[['id',poin['xor']]],['id',poin['and']+2]])
        poin['not']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[inp1[1],['id',poin['not']-3]],['id',poin['or']]])
        poin['and']+=1
        addr=[['id',poin['xor']],poin['not']-1]
        tmp_table.append([addr,[inp1[1],inp2[1]],['id',poin['not']-1]])
        poin['xor']+=1
        addr=[['id',poin['and']],poin['and']+1]
        tmp_table.append([addr,[inp1[0],['id',poin['not']-2]],['id',poin['and']+1]])
        poin['and']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[['id',poin['not']-1],['id',poin['and']-1]],['id',poin['or']]])
        poin['and']+=1
        addr=[['id',poin['or']],oup[0]]
        tmp_table.append([addr,[['id',poin['and']-3],['id',poin['and']-1]],oup[0]])
        poin['or']+=1
        return tmp_table

def sthan(inp1,inp2,oup):
    global poin
    tmp_table=[]
    if poin['not']>1015 or poin['or']>1005 or poin['and']>1009 or poin['xor']>1023:
        print('ERROR: Space Not Enough')
        return -1
    else:
        addr=[['id',poin['not']],poin['and']]
        tmp_table.append([addr,[inp1[1]],['id',poin['and']]])
        poin['not']+=1
        addr=[['id',poin['not']],poin['and']+1]
        tmp_table.append([addr,[inp1[0]],['id',poin['and']+1]])
        poin['not']+=1
        addr=[['id',poin['not']],poin['and']+2]
        tmp_table.append([addr,[['id',poin['xor']]],['id',poin['and']+2]])
        poin['not']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[['id',poin['not']-3],inp2[1]],['id',poin['or']]])
        poin['and']+=1
        addr=[['id',poin['xor']],poin['not']-1]
        tmp_table.append([addr,[inp1[1],inp2[1]],['id',poin['not']-1]])
        poin['xor']+=1
        addr=[['id',poin['and']],poin['and']+1]
        tmp_table.append([addr,[['id',poin['not']-2],inp2[0]],['id',poin['and']+1]])
        poin['and']+=1
        addr=[['id',poin['and']],poin['or']]
        tmp_table.append([addr,[['id',poin['not']-1],['id',poin['and']-1]],['id',poin['or']]])
        poin['and']+=1
        addr=[['id',poin['or']],oup[0]]
        tmp_table.append([addr,[['id',poin['and']-3],['id',poin['and']-1]],oup[0]])
        poin['or']+=1
        return tmp_table


    
### 内部算法结束
    
def d_gene(incode):
    
    tmp_table=[]
    tmp_ins=[]# 暂存指令
    instr=[] #存放最终产生的指令
    idnum=len(incode)*2
    global poin
    #当前指针
    var=[] #暂时存放输出变量，直到最后要求输出那个再输出
    varpoi=0#变量指针序号
    numin=0 #输入变量的个数
    for i in range(10): #contain variables
        dic={'id':'','value':0}
        var.append(dic)
    #print(var)

    #############
    ##把每一句拆成2bit格式的    
    nincode=[] # new generated code
    for cod in incode:
        ncod=incd()
        ncod.num=[cod.num*2-1,cod.num*2]
        ncod.type=cod.type
        if not cod.in1:
            ncod.in1=[]
        elif cod.in1[0]=='id':
            if type(cod.in1[1])== int:
                ncod.in1=[[cod.in1[0],cod.in1[1]*2-1],[cod.in1[0],cod.in1[1]*2]]
            else:
                ncod.in1=[[cod.in1[0],cod.in1[1]+'_0'],[cod.in1[0],cod.in1[1]+'_1']]
        elif cod.in1[0]=='num':
            b0=int(cod.in1[1])%2
            b1=math.floor (int(cod.in1[1])/2)
            ncod.in1=[['num',b0],['num',b1]]
        else:
            ncod.in1=[]
        if not cod.in2:
            ncod.in2=[]   
        elif cod.in2[0]=='id':
            if type(cod.in2[1])== int:
                ncod.in2=[[cod.in2[0],cod.in2[1]*2-1],[cod.in2[0],cod.in2[1]*2]]
            else:
                ncod.in2=[[cod.in2[0],cod.in2[1]+'_0'],[cod.in2[0],cod.in2[1]+'_1']]
        elif cod.in2[0]=='num':
            b0=int(cod.in2[1])%2
            b1=math.floor (int(cod.in2[1])/2)
            ncod.in2=[['num',b0],['num',b1]]
        else:
            ncod.in2=[]

        if not cod.in3:
            ncod.in3=[]
        elif cod.in3[0]=='id':
            if type(cod.in3[1])== int:
                ncod.in3=[[cod.in3[0],cod.in3[1]*2-1],[cod.in3[0],cod.in3[1]*2]]
            else:
                ncod.in3=[[cod.in3[0],cod.in3[1]+'_0'],[cod.in3[0],cod.in3[1]+'_1']]
        elif cod.in3[0]=='num':
            b0=int(cod.in3[1])%2
            b1=math.floor (int(cod.in3[1])/2)
            ncod.in3=[['num',b0],['num',b1]]
        else:
            ncod.in3=[]
        nincode.append(ncod)
        #print(ncod.num,ncod.type ,ncod.in1 ,ncod.in2, ncod.in3 )
##    for co in nincode:
##        print(co.num,co.type ,co.in1 ,co.in2, co.in3 ) 
    ######拆分结束
    ####对新的incode进行分析
    for co in nincode:
        #print(co,len(co))
        if co.type=='if':#对if语句的拆解
            tmp_ins.append(['FLAG',co.in2[0],co.in1[0]])
            tmp_ins.append(['FLAG',co.in2[1],co.in1[0]])
            print(co.num,co.type ,co.in1 ,co.in2, co.in3 )
            
            inp=[co.in1[0]]
            addr=[['id',poin['not']],idnum] #addr 用来建立输入与输出之间的联络，暂存于tmp_table
            poin['not']=poin['not']+1 #指针移动，无法判断是否走过了
            idnum=idnum+1
            tmp_table.append([addr, inp,idnum])
            tmp_ins.append(['FLAG',co.in3[0],['id',poin['not']-1]])
            tmp_ins.append(['FLAG',co.in3[1],['id',poin['not']-1]])
        elif co.type=='while': # 对while句的拆解
            addr=poin['whil']
        elif co.type=='=': #赋值语句
            #print(co)
            addr=['var %d'%varpoi,co.num[0]]
            var[varpoi]['id']=co.in1[0]
            var[varpoi]['value']=co.in2[0]
            varpoi+=1
            inp=[co.in2[0]]
            oup=co.num[0]
            tmp_table.append([addr, inp,oup])
            addr=['var %d'%varpoi,co.num[1]]
            var[varpoi]['id']=co.in1[1]
            var[varpoi]['value']=co.in2[1]
            varpoi+=1
            inp=[co.in2[1]]
            oup=co.num[1]
            tmp_table.append([addr, inp,oup])
        elif co.type in ['and','or','xor','not','nor','xnor','nand']:
            #逻辑运算
            inp1=co.in1
            inp2=co.in2
            oup=co.num
            if co.type=='and':
                tmp_table.extend(dand(inp1,inp2,oup))
            elif co.type=='or':
                tmp_table.extend(dor(inp1,inp2,oup))
            elif co.type=='xor':
                tmp_table.extend(dxor(inp1,inp2,oup))
            elif co.type=='not':
                tmp_table.extend(dnot(inp2,oup))
            elif co.type=='xnor':
                tmp_table.extend(dxnor(inp1,inp2,oup))
            elif co.type=='nand':
                tmp_table.extend(dnand(inp1,inp2,oup))
            elif co.type=='nor':
                tmp_table.extend(dnor(inp1,inp2,oup))
        elif co.type in ['==','!=','>','<','>=','<=']: # 关系运算
            # not finished
            inp1=co.in1
            inp2=co.in2
            oup=co.num
            if co.type=='==':
                tmp_table.extend(eq(inp1,inp2,oup))
            elif co.type=='!=':
                tmp_table.extend(neq(inp1,inp2,oup))
            elif co.type=='>':
                tmp_table.extend(lthan(inp1,inp2,oup))
            elif co.type=='<':
                tmp_table.extend(sthan(inp1,inp2,oup))
            
  

        elif co.type in ['+','-','*','/']: #算数运算
            inp1=co.in1
            inp2=co.in2
            oup=co.num
            if co.type=='+':
                
                tmp_table.extend(adder(inp1,inp2,oup))
            elif co.type=='-':
                tmp_table.extend(sub(inp1,inp2,oup))
            elif co.type=='*':
                tmp_table.extend(mul(inp1,inp2,oup))
            elif co.type=='/':
                tmp_table.extend(div(inp1,inp2,oup))
##        else :
##            addr=[poin[co[3]],co[0]]
##            poin[co[3]]=poin[co[3]]+1
##            inp=[co[2],co[4]]
##            oup=co[0]
##            tmp_table.append([addr, inp,oup])
##    print(tmp_table)
##    print(var)
    #处理FLAG部分
    for ins in tmp_ins:
        if ins[0]=='FLAG':
            print(ins)
            id1=ins[1][1]
            id2=ins[2][1]
            print((id1))
            if id2>100:
                addr2=id2
            else:
                for tmp in tmp_table:
                    oid1=tmp[0][1]
                    if id2==oid1:
                        addr2=tmp[0][0]
            for tmp in tmp_table:
                oid1=tmp[0][1]
                
                if id1==oid1:
                    print(oid1,id1,id2)
                    addr1=tmp[0][0]
##                elif id2==oid1:
##                    addr2=tmp[0][0]
            print(addr1,addr2)
            instr.append(['FLAG',addr1,addr2])
    #处理临时表
    # print('tmp table')
    # for tmp in tmp_table:
    #     print(tmp)
    for tmp in tmp_table:
        add2=tmp[0][0][1]
##        print((tmp))
##        print(instr)
##        if isinstance(tmp[0][0],int):
        for i in range(len(tmp[1])):
            #两个input
##            print('****')
##            print(tmp[1][i])
            if 'id' in tmp[1][i] and 'var' not in tmp[0][0]: #输入中包含id的
                add1=tmp[1][i][1]
                #print('add1',add1)
                if type(add1)==str:
                    #如果id后面是一个变量名,表示需要输入input
                    add1=numin
                    vname=tmp[1][i][1]
                    instr.append('WIR1(%s,%s,%d)'%(vname,add2,i))
                    # toapp='WIR1(%s,%d)'%(vname,numin) #等待append
                    # totest='WIR1(%s'%(vname)#等待判断是否已经输入
                    # tmpf=0 #临时flag
                    # lo=0 #所在位置
                    # for ins in instr:
                    #     #print(ins)
                    #     if totest in ins:
                    #         tmpf=1
                    #         break
                    #     else:
                    #         lo+=1
                    # #print('lo',lo)        
                    # if not tmpf :
                    #     instr.append(toapp)
                    #     instr.append('WIR1(%s,%s,%d)'%(vname,add2,i))
                    #     numin=numin+1
                    # else:
                    #     #如果变量表中已经有这个变量了。
                    #     instr.append('WIR1(%d,%s,%d)'%(int(ins.split(',')[1].split(')')[0]),add2,i))
                    
                    
                else:
                    #在临时表中寻找输出的位置
                    for ntmp in tmp_table:
                        oid1=ntmp[0][0][1] #地址直接以端口号表示
                        oid2=ntmp[0][1]  # 地址以程序编号表示
                        #print(oid1,add1)
                        if oid1==add1 or oid2==add1:
                            instr.append('WIR2(%s,%s,%d)'%(ntmp[0][0][1],add2,i))
                            #print('WIR2(%s,%s,%d)'%(ntmp[0][0],add2,i))
                            break
                    
            elif 'num'in tmp[1][i]:
                num=tmp[1][i][1]
                instr.append('WIR2([num,%d],%s,%d)'%(num,add2,i))
##            else :
##                print('error')
##            print(tmp)
##            print(instr)
        vi=0
    #处理临时变量
    for va in var[0:varpoi]:
        vi+=1
##        print('***************')
##        print(va)
        if 'id' in va['value']:
            vid=va['value'][1]
            f=0
            for tmp in tmp_table:
                oid1=tmp[0][1]
                if oid1==vid:
                    instr.append('WIR3(%s,%s,%d)'%(va['id'][1],tmp[0][0][1],vi-1))
                    f=1
                    break
            if f==0:
                instr.append('WIR3(%s,%s,%d)'%(va['id'][1],va['value'],vi-1))
        else:
            instr.append('WIR3(%s,%s,%d)'%(va['id'][1],va['value'][1],vi-1))
            
    
    print()
    #inp与var的连接
    pos=[]
    for ins in instr:
        if 'INP' in ins:
            i_name=ins.split('(')[1].split(',')[0]
            i_po=ins.split(',')[1].split(')')[0] # 在input寄存器中的位置
            for inn in instr[0:len(instr)-2]:
                if 'VAR' in inn:
                    v_name=inn.split('(')[1].split(',')[0]
                    v_f=inn.split(',')[1]
                    if i_name==v_name:
                        
                        pos.append(instr.index(inn))
                        pos.append(instr.index(ins))
                        for inns in instr:
                            if ('WIR1' in inns ):
                                f=inns.split('(')[1].split(',')[0]
                                
                                if f==i_po:
                                    t=inns.split(',')[1]
                                    pnum=inns.split(',')[2].split(')')[0]
                                    po=instr.index(inns)
                                    
                                    instr[po]='WIR2(%s,%s,%s)'%(v_f,t,pnum)
    nins=[]
    for ins in instr:
        if instr.index(ins) not in pos:
            nins.append(ins)
            print(ins)
    return instr

###
### for testing
####cod=['2 :  [num,3] == [num,3]', '3 :  [id,b] = [num,3]',\
####     '5 :  [id,a] + [num,2]','4 :  [id,b] = [id,5]',\
####     '1 :  if [id,2] : [id,3] else : [id,4]']
##cod=['5 :  [id,a] + [num,2]']
##tabl=d_gene(cod)
##for ta in tabl:
##    print(ta)
