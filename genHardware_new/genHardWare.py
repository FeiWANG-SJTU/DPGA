#generate hardware from 'ncDomain.txt'
import logicGate3s
import inpAndOupt
import modules
import sqlite3
f=open('af_5base.txt','r')
cdomain=[] 
po=0 #position

for line in f:
    cdomain.append(line.strip('\n'))
    #cdomain.append(line.strip('\r'))
print('lib length',len(cdomain))

##########################
# Logic gate
mods=[] # for saving modules
for i in range(6):
    mods.append(logicGate3s.gen_lgat(1,i,cdomain[po:po+5]))
    po=po+5

for i in range(6):
    mods.append(logicGate3s.gen_lgat(2,i+4,cdomain[po:po+5]))
    po=po+5
for i in range(6):
    mods.append(logicGate3s.gen_lgat(3,i+8,cdomain[po:po+6]))
    po=po+6
for i in range(6):
    mods.append(logicGate3s.gen_lgat(4,i+12,cdomain[po:po+4]))
    po=po+4
##for mod in mods:
##    print(mod.out)
    
###############
# input and output
##inpts=[]
oupts=[]
##for i in range(10):
##    inp=inpAndOupt.gen_inp (i,cdomain[po:po+2])
##    po+=2
##    inpts.append(inp)
for i in range(6):    
    oup=inpAndOupt.gen_oup (i,cdomain[po:po+2])
    po+=2
    oupts.append(oup)
##print('************************************')
##for inp in inpts:
##    inp.show()
##print('************************************')
##for oup in oupts:
##    oup.show()
###################
# ADPs
adps=[]
adpnum=0
for i in range(len(mods)):
    for j in range (len(mods)):
        if i !=j:
           ad1=modules.adap(1,i,j,0)
           ad1.setSeq1(mods)
           ad1.num=adpnum
           adps.append(ad1)
           adpnum+=1
           if mods[j].typ !='not':
               ad2=modules.adap(1,i,j,1)
               ad2.setSeq1(mods)
               ad2.num=adpnum
               adps.append(ad2)
               adpnum+=1

for i in range(len(oupts)):
    for j in range (len(mods)):
       ad1=modules.adap(2,j,i,0)
       ad1.setSeq2(mods,oupts)
       ad1.num=adpnum
       adps.append(ad1)
       adpnum+=1
       
##for adp in adps:
##    adp.show()
##########################
##threshold



       
#for adp in adps:
#    adp.show()
print('used seqs',po+1)
conn = sqlite3.connect('hardwaredb_new.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Ouputs;
DROP TABLE IF EXISTS LogicGates;
DROP TABLE IF EXISTS Adaptors;

CREATE TABLE Ouputs (
    num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    OU0 TEXT,
    OU1 TEXT
);
CREATE TABLE LogicGates (
    num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    type TEXT,
    s1 TEXT,
    s2 TEXT,
    s3 TEXT,
    s4 TEXT,
    s5 TEXT,
    s6 TEXT,
    s7 TEXT,
    s8 TEXT,
    s9 TEXT,
    s10 TEXT
    
);

CREATE TABLE Adaptors (
    num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    type INTEGER,
    onum INTEGER,
    inum INTEGER,
    portnumber INTEGER,
    s1 TEXT,
    s2 TEXT,
    s3 TEXT,
    s4 TEXT,
    s5 TEXT,
    s6 TEXT,
    s7 TEXT,
    s8 TEXT,
    s9 TEXT,
    s10 TEXT
)
''')
##for inp in inpts:
##    cur.execute('''INSERT OR IGNORE INTO Inputs(num,IN0,IN1)
##        VALUES(?, ?,?)''',(inp.num,inp.seq[0],inp.seq[1]))
##    conn.commit()
for oup in oupts:
    cur.execute('''INSERT OR IGNORE INTO Ouputs(num,OU0,OU1)
        VALUES(?, ?,?)''',(oup.num,oup.seq[0],oup.seq[1]))
    conn.commit()
for mod in mods:
    tseq=mod.gate_seq
    if mod.typ in ['and','or']:
        cur.execute('''INSERT OR IGNORE INTO LogicGates(
            num,type,s1,s2,s3,s4,s5) VALUES(?,?,?,?,?,?,?)'''
                ,(mod.num,mod.typ,tseq[0],tseq[1],tseq[2],tseq[3],tseq[4]))
    elif mod.typ=='not':
        cur.execute('''INSERT OR IGNORE INTO LogicGates(
            num,type,s1,s2,s3,s4) VALUES(?,?,?,?,?,?)'''
                ,(mod.num,mod.typ,tseq[0],tseq[1],tseq[2],tseq[3]))
        
    if mod.typ=='xor':
        cur.execute('''INSERT OR IGNORE INTO LogicGates(num,type,s1,s2,s3,s4,
            s5,s6,s7,s8,s9,s10) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(\
            mod.num,mod.typ,tseq[0],tseq[1],\
            tseq[2],tseq[3],tseq[4],tseq[5],tseq[6],tseq[7],\
            tseq[8],tseq[9]))
    conn.commit()

for adp in adps:
    q=adp.seq
    cur.execute('''INSERT OR IGNORE INTO Adaptors(
        num,type,onum,inum,portnumber,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
        VALUES(?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
                ,(adp.num,adp.typ,adp.bfnum,adp.afnum,adp.portnum, \
                  q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9]))
    conn.commit()
conn.close()
