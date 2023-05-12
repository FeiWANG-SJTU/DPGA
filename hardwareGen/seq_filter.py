# function: filter initial generated seqs
# by OL , Feb 23, 2016
from random import shuffle
def hamming_distance(s1, s2):
    #Return the Hamming distance between equal-length sequences
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def subword_dist(x,y):
    #使用动态规划算法
    import numpy as np
    
    l1=len(x)
    l2=len(y)
    m=np.zeros([l1,l2]) # 存放每个位置的比对结果
    for i in range(l2):
        if x[0]==y[i]:
            m[0][i]=1
    for i in range(l1):
        if y[0]==x[i]:
            m[i][0]=1
    for i in range(1,l1):
        for j in range(1,l2):
            if x[i]==y[j]:
                m[i][j]=m[i-1][j-1]+1
    mlen=np.max(m)
    #print(m)
    return mlen  #return the maxium subword length
def same_length(x,y):
    l=len(x)
    cmp=[]
    tmp=0
    le=0
    for i in range(l):
        if x[i]==y[i]:
            cmp.append(1)
        else:
            cmp.append(0)
    st=0
    for i in range(len(cmp)):
        if (i==0 and cmp[i]==1) or (i>0 and cmp[i-1]==0 and cmp[i]==1):
            st=i
        if i==l-1 and cmp[i]==1:
            le=l-st
        elif i>1 and cmp[i]==0 and cmp[i-1]==1:
            le=i-st
        if le>tmp:
            tmp=le
    return tmp
def same_le_st(x,y):
    l=len(x)
    cmp=[]
    tmp=0
    le=0
    for i in range(l):
        if x[i]==y[i]:
            cmp.append(1)
        else:
            cmp.append(0)
    st=0
    tst=0
    for i in range(len(cmp)):
        if (i==0 and cmp[i]==1) or (i>0 and cmp[i-1]==0 and cmp[i]==1):
            st=i
        if i==l-1 and cmp[i]==1:
            le=l-st
        elif i>1 and cmp[i]==0 and cmp[i-1]==1:
            le=i-st
        if le>tmp:
            tmp=le
            tst=st
    return tst
##a='AATTCCAAC'
##b='ATTTCAACC'
##print(subword_dist(a,b))
##f=open('cDomain.txt','r')
####print(f.readline().strip('\n'))
##ndomain=[]
##i=0
##for line in f :
####    print (line)
##    if 'AAAA'  in line:
##        #print(line)
##        continue
##    elif 'CCC' in line:
##        continue
##    elif 'GGG' in line :
##        continue
##    elif 'TTTT' in line:
##        continue
##    elif line.count('C')+line.count('G')<4 or line.count('C')+line.count('G')>8:
##        continue
##    else :
##        ndomain.append(line.strip('\n'))
##        i=i+1
###hamming distance >7 & subword
##f.close()
##seed='ACTCTCCACTCA'
##for dom in ndomain :
##    if hamming_distance(seed,dom)<4:
##        ndomain.remove(dom)
##ndomain.append(seed)
##shuffle(ndomain)

##ff=open('afhamming.txt','w')
##ff.write('\n'.join(ndomain))
##ff.close()
##f=open('afhamming.txt','r')
##nndomain=[]
##nnum=1
##nndomain.append(f.readline().strip('\n'))
##loc=0
##for line in f:
##    loc+=1
##    if loc%1000==0:
##        print(loc)
##    dom=line.strip('\n')
##    flag=0
##    #print(ii)
##    for iii in range(nnum):
##        a=hamming_distance(dom,nndomain[iii]) #hamming distance
##        if a<4:
##            flag=1
##            break
##        b=subword_dist(dom,nndomain[iii])  #subword
##        if b>7 :
##            flag=1
##            break
##        c=same_length(dom,nndomain[iii]) # max same length
##        if c>5:
##            flag=1
##            break
##    #print(flag)
##    if flag==0:
##        nndomain.append(dom)
##        nnum+=1
##           
##print(len(nndomain))   
##nf=open('ncDomain.txt','w')
##nf.write('\n'.join(nndomain))
##nf.close()

##如果中间有五个碱基相同，必须保证两边的两个都不含有TC，防止形成TG键
f=open('ncDomain.txt','r')
nndomain=[]
nnum=1
nndomain.append(f.readline().strip('\n'))
for line in f:
    
    dom=line.strip('\n')
    flag=0
    #print(ii)
    for iii in range(nnum):
        c=same_length(dom,nndomain[iii]) # max same length
        if c==5:
            st=same_le_st(dom,nndomain[iii])
            if st>0 and st<7:
                if dom[st-1]=='T' and nndomain[iii][st-1]=='C':
                   flag=1
                   break
                if dom[st-1]=='C' and nndomain[iii][st-1]=='T':
                   flag=1
                   break
                if dom[st+5]=='T' and nndomain[iii][st+5]=='C':
                   flag=1
                   break
                if dom[st+5]=='C' and nndomain[iii][st+5]=='T':
                   flag=1
                   break
            
    #print(flag)
    if flag==0:
        nndomain.append(dom)
        nnum+=1
           
print(len(nndomain))   
nf=open('af_5base.txt','w')
nf.write('\n'.join(nndomain))
nf.close()
