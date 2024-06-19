#function: generate changable domain 11 nt
#output: all possible sequence without filtering
# by O.L. Feb 15,2016
dic={0:'A',1:'C',2:'T'}
a=[]
l=[] # for storing letters
cDomain=[]
f=open('cDomain.txt','w')
for i in range(12) :
    a.append(i)
    l.append('')
for i in range(3**12) :
    tmp=0
    for j in range(12) :
        a[j]=int(((i-tmp)/3**j)%(3))
        tmp=tmp+a[j]*3**j
        #print(a[j])
        l[j]=dic[a[j]]
    #print(l)
    c=''.join(l)
    cDomain.append(c)
    #f.writelines(c)

#print(cDomain)

f.write('\n'.join(cDomain))
f.close()
