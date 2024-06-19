# function : reverse, complement of a DNA sequence
# by O.L , Sept.16, 2015
def rev_comp(seq):
    l=len(seq)
    nseq=[]
    for i in range(l):
        if seq[i]=='A':
            nseq.append('T')
        elif seq[i]=='T':
            nseq.append('A')
        elif seq[i]=='C':
            nseq.append('G')
        elif seq[i]=='G':
            nseq.append('C')
        else:
            print ('warn: Not a DNA sequence!!!')
            return
    nseq.reverse()
    rcseq=''.join(nseq)
    return rcseq

# example for test
# a='AAGfCCG'
# b=rev_comp(a)
# print(b)
