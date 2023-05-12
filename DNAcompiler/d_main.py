# main program of this DNA complier
# user input: need a blank space after each word
# by OL Jan. 12 , 2016
import d_lexer1
import d_parser
import d_ast1
import d_inte_gene
import d_gene
mypro=input('Enter your program:')
#print(mypro)
tokens=d_lexer1.d_lex(mypro)

root=d_ast1.tree('headers')
headers=d_parser.d_par(tokens)
for header in headers:
    #print(type(header),header.data)
    if header.id==1:
        root.add(header)
        #print(header)
#print(root.getchildren())
cod=d_inte_gene.in_gene(headers)
ins=d_gene.d_gene(cod)
print('************************************')
print('user program:')
print()
print(mypro)

print('************************************')

print('token stream :')
print()
for token in tokens:
    print(token)
    

print('***********************************************')
print('intermediate code :')
print()
for co in cod:
    print(co)          

print()
print('***********************************************')
print('instructions:')
print()
for inn in ins:
    print(inn)
