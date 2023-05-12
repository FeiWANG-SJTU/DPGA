class node:
    #端点节点，包括变量和数字
 
    def __init__(self, data):
        self.num=data[0][0]
        self.id = data[0][1]
        self.children = []
 
    def getdata(self):
        return self._data
 
    def getchildren(self):
        return self.children
 
    def add(self, node):
        ##if full
        if len(self.children) == 4:
            return False
        else:
            self.children.append(node)
class tree:
    #根节点
    def __init__(self, data):
        
        self.id=0
        self.data = data
        self.children = []
 
    def getdata(self):
        return self._data
 
    def getchildren(self):
        return self.children
 
    def add(self, node):
        ##if full
        if len(self.children) == 4:
            return False
        else:
            self.children.append(node)
 
class If:
    def __init__(self, condition, true_stmt,false_stmt):
        self.condition=condition
        self.true_stmt=true_stmt
        self.false_stmt=false_stmt
        self.data='if'
        self.cchild=[]
        self.tchild=[]
        self.fchild=[]
        self.id=0
        self.num='id'
    def addcchild(self,node):  # child 
        self.cchild.append(node)
    def addtchild(self,node):
        self.tchild.append(node)
    def addfchild(self,node):
        self.fchild.append(node)
    def eval(self, env):  ##????
        condition_value = self.condition.eval(env)
        if condition_value:
            self.true_stmt.eval(env)
        else:
            if self.false_stmt:
                self.false_stmt.eval(env)

class For :
    def __init__ (self, strt, stp, condition_varible, body):
        self.strt=strt
        self.stp=stp
        self.condition_vari=condition_varible
        self.body=body
        self.data='for'
        self.id=0
        self.num='id'
        self.child=[]
    def addchild(self,nod):
        self.child.append(node)

class Whil:
    def __init__(self, condition, body):
        self.data='while'
        self.condition = condition
        self.body = body
        self.cchild=[]
        self.bchild=[]
        self.id=0
        self.num='id'
    def addcchild(self,node):
        self.cchild.append(node)
    def addbchild(self,node):
        self.bchild.append(node)
class AssignStmt:
    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp
        self.data= '='
        self.achild=[]
        self.nchild=[]
        self.id=0
        self.num='id'
    def addachild(self,node):
        self.achild.append(node)
    def addnchild(self,node):
        self.nchild.append(node)    
class Rel:
    def __init__(self,expr1,expr2,op):
        self.data=op
        self.rel1=expr1
        self.rel2=expr2
        self.lchild=[]
        self.rchild=[]
        self.id=0
        self.num='id'
    def addlchild(self,node):
        self.lchild.append(node)
    def addrchild(self,node):
        self.rchild.append(node)
class Log(): #逻辑表达式
    def __init__(self,expr1,expr2,op):
        self.data=op
        self.log1=expr1
        self.log2=expr2
        self.lchild=[]
        self.rchild=[]
        self.id=0
        self.num='id'
    def addlchild(self,node):
        self.lchild.append(node)
    def addrchild(self,node):
        self.rchild.append(node)
class Expr(): #表达式 add
    def __init__(self,expr1,term,op):
        self.data=op
        self.expr1=expr1
        self.term=term
        self.echild=[]
        self.tchild=[]
        delf.id=0
        self.num='id'
    def addechild(self,node):
        self.echild.append(node)
    def addtchild(self,node):
        self.tchild.append(node)
class Term(): 
    def __init__(self,term1,factor1,op):
        self.data=op
        self.term=term1
        self.factor=factor1
        self.tchild=[]
        self.fchild=[]
        self.id=0
        self.num='id'
    def addtchild(self,node):
        self.tchild.append(node)
    def addfchild(self,node):
        self.fchild.append(node)
class Factor():
    def __init__(self,factor1,ter,op):
        self.data=op
        self.factor=factor1
        self.ter=ter
        self.id=0
        self.fchild=[]
        self.tchild=[]
        self.num='id'
    def addfchild(self,node):
        self.fchild.append(node)
    def addtchild(self,node):
        self.tchild.append(node)
