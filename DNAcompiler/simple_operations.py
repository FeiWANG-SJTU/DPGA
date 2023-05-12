# function: methods to compile simple operations
# by O.L., Jul 6, 2016
# modified Sep 3, 2016
# input : inp1, inp2, oup1
# output: tmp_table, tmp_instr
# 去掉type1连接器，因为所有的指令都是连接，所以每一句tmp_table生成的时候需要交代清楚in-ou的关系即可
# global variables: pointers

# arithmetic operations
def adder(inp1,inp2,oup1):
    global poin
    global varpoin # 临时输出变量的指针
    tmp_table=[]
    # compiling of 1bit full adder
    if poin['xor']>14 or poin['and']>6: # pointer for and xor
        print( 'ERROR: SPACE not enough')
        return -1
    else :
        addr=[poin['xor'],co[0]]
        poin['xor']+=1
        inp=[inp1,inp2]
        oup=co[0]
        tmp_table.append([addr,inp,oup])
        return tmp_table
##def adder(inp1,inp2,oup1):
##    global poin
##    global varpoin # 临时输出变量的指针
##    global tmp_table
##    # compiling of 1bit full adder
##    if poin['xor']>14 or poin['and']>6: # pointer for and xor
##        print( 'ERROR: SPACE not enough')
##        return -1
##    else :
##        if inp1[0]=='num' or if type(inp1[1]=='str'): # 从inp直接输入
##            ins.append('INP( %s , %d , 0 )' %(inp1,poin['xor']))
##            #ins.append('INP( %s , %d , 0 )' %(inp1,poin['and']))
##            
##        else :
##            ins.append(' WIR1 ( %d , %d , 0 )' %(inp1[1], poin['xor']))
##            #ins.append(' WIR1 ( %d , %d , 0 )' %(inp1[1], poin['and']))
##                       
##        if inp2[0]=='num' or if type(inp2[1]=='str'):
##            ins.append('INP( %s , %d , 1 )' %(inp2,poin['xor']))
##            #ins.append('INP( %s , %d , 1 )' %(inp2,poin['and']))
##        else :
##            ins.append(' WIR1 ( %d , %d , 1 )' %(inp2[1], poin['xor']))
##            #ins.append(' WIR1 ( %d , %d , 1 )' %(inp2[1], poin['and']))
##        return 
def suber(inp1,inp2,oup1):

    return ins

def div(inp1,inp2,oup1):

    return ins

def mul(inp1,inp2,oup1):

    return ins

# logic operations


# relation operations
def lthan(inp1,inp2,oup1):

    return ins

def sthan(inp1,inp2, oup1):

    return ins

def eql(inp1, inp2, oup1):

    return ins
                   
def neql(inp1, inp2, oup1):

    return ins

