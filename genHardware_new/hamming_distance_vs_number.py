#filtered sequence 
import numpy as np

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


##main function
f=open('af_5base.txt','r')
po=0 #position
cdomain=[]
for line in f:
    cdomain.append(line.strip('\n'))
    #cdomain.append(line.strip('\r'))
print('lib length',len(cdomain))

subwordd=[]
subwordd.append([subword_dist(cdomain[0],cdomain[1])])

for i in range(2,100,1):
    temp=[]
    for j in range(i):
        a=subword_dist(cdomain[i], cdomain[j])
        temp.append(a)
        #print(temp)
    subwordd.append(temp)
    #print(subwordd) 

ave=[]
stdd=[] 
subwordd[1].append(int(subwordd[0][0]))     
for i in range(2,99,1):
    subwordd[i].extend(subwordd[i-1])
for i in range(99):
    ave.append(np.max(subwordd[i]))
    stdd.append(np.std(subwordd[i]))    
        

# #random generate sequence 
# import numpy as np
# import rand_gene_dna_seq as rd

# def subword_dist(x,y):
#     #使用动态规划算法
    
#     l1=len(x)
#     l2=len(y)
#     m=np.zeros([l1,l2]) # 存放每个位置的比对结果
#     for i in range(l2):
#         if x[0]==y[i]:
#             m[0][i]=1
#     for i in range(l1):
#         if y[0]==x[i]:
#             m[i][0]=1
#     for i in range(1,l1):
#         for j in range(1,l2):
#             if x[i]==y[j]:
#                 m[i][j]=m[i-1][j-1]+1
#     mlen=np.max(m)
#     #print(m)
#     return mlen  #return the maxium subword length
# def hamming_distance(s1, s2):
#     #Return the Hamming distance between equal-length sequences
#     if len(s1) != len(s2):
#         raise ValueError("Undefined for sequences of unequal length")
#     return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# ##main function

# cdomain=[]
# for i in range (100):
#     a=rd.rand_seq(12)
#     cdomain.append(''.join(a))


# subwordd=[]
# subwordd.append([subword_dist(cdomain[0],cdomain[1])])

# for i in range(2,100,1):
#     temp=[]
#     for j in range(i):
#         a=subword_dist(cdomain[i], cdomain[j])
#         temp.append(a)
#         #print(temp)
#     subwordd.append(temp)
#     #print(subwordd) 

# ave=[]
# stdd=[] 
# subwordd[1].append(int(subwordd[0][0]))   
# for i in range(2,99,1):
#     subwordd[i].extend(subwordd[i-1])
# for i in range(99):
#     ave.append(np.max(subwordd[i]))
#     stdd.append(np.std(subwordd[i]))    
ave=[]
for i in range(99):
    ave.append((ave1[i]+ave2[i]+ave3[i])/3)        