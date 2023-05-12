#function: generate intermediate cod_for_printe
# imput : syntax tree
# output: intermediate cod_for_print, cod 
# by OL , sep 3, 2016
class incd:
    #一行中间代码
    def __init__(self):
        self.num=0
        self.type=''
        self.in1=[]
        self.in2=[]
        self.in3=[]
def in_gene(headers):
    cod_for_print=[]
    cod=[]
    for header in headers:
        
        
        if header.data=='if': #如果是if节点
            a='%s : if [%s,%s] : [%s,%s] else : [%s,%s]'%(header.id,header.cchild[0].num,header.cchild[0].id,\
                                                       header.tchild[0].num,header.tchild[0].id,\
                                                      header.fchild[0].num, header.fchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type='if'
            co.in1=[header.cchild[0].num,header.cchild[0].id]
            co.in2=[header.tchild[0].num,header.tchild[0].id]
            co.in3=[header.fchild[0].num,header.fchild[0].id]
            cod.append(co)
        elif header.data=='while': #while节点
            a='%s  :  while [%s,%s]:[%s,%s]'%(header.id,header.cchild[0].num,header.cchild[0].id,\
                                           header.bchild[0].num,header.bchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type='while'
            co.in1=[header.cchild[0].num,header.cchild[0].id]
            co.in2=[header.bchild[0].num,header.bchild[0].id]
            cod.append(co)
        elif header.data =='=': #赋值运算
            a='%s  :  [%s,%s] = [%s,%s]'%(header.id,header.nchild[0].num,header.nchild[0].id,\
                                       header.achild[0].num,header.achild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type='='
            co.in1=[header.nchild[0].num,header.nchild[0].id]
            co.in2=[header.achild[0].num,header.achild[0].id]
            cod.append(co)
        elif header.data in ['==','!=','<=','>=','<','>']: #关系运算
            a='%s  :  [%s,%s] %s [%s,%s]'%(header.id,header.lchild[0].num,header.lchild[0].id,\
                                       header.data,header.rchild[0].num,header.rchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type=header.data
            co.in1=[header.lchild[0].num,header.lchild[0].id]
            co.in2=[header.rchild[0].num,header.rchild[0].id]
            cod.append(co)
        elif header.data in ['and','or','xor','nor','xnor','nand']:#逻辑运算
            a='%s  :  [%s,%s] %s [%s,%s]'%(header.id,header.lchild[0].num,header.lchild[0].id,\
                                        header.data , header.rchild[0].num,header.rchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type=header.data
            co.in1=[header.lchild[0].num,header.lchild[0].id]
            co.in2=[header.rchild[0].num,header.rchild[0].id]
            cod.append(co)
        elif header.data=='not':
            a='%s  : %s [%s,%s]'%(header.id,header.data , header.rchild[0].num,header.rchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type=header.data
            co.in2=[header.rchild[0].num,header.rchild[0].id]
            cod.append(co)
        elif header.data in ['+','-']: #
            a='%s  :  [%s,%s] %s [%s,%s]'%(header.id,header.tchild[0].num,header.tchild[0].id,\
                                        header.data,header.fchild[0].num,header.fchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type=header.data
            co.in1=[header.tchild[0].num,header.tchild[0].id]
            co.in2=[header.fchild[0].num,header.fchild[0].id]
            cod.append(co)
        elif header.data in ['*','/']:
            #print(header.id,header.fchild)
            a='%s  :  [%s,%s] %s [%s,%s]'%(header.id,header.fchild[0].num,header.fchild[0].id,\
                                        header.data,header.tchild[0].num,header.tchild[0].id)
            cod_for_print.append(a)
            co=incd()
            co.num=header.id
            co.type=header.data
            co.in1=[header.fchild[0].num,header.fchild[0].id]
            co.in2=[header.tchild[0].num,header.tchild[0].id]
            cod.append(co)
    print('*'*30)
    print('intermediate code:')
    for codd in cod_for_print:
        print(codd)
    return cod




