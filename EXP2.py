import sys
import numpy as np#imports numpy a n dimensional array object
import math
c=sys.argv[1]
with open(c) as f:
    l = f.readlines()
words = []
k=p=m=0;omega=0
for a in range(len(l)):
    if l[a].startswith('.circuit'):#checks whether .circuit is present and returns its index to k
        k=a
for e in range(len(l)):
    if l[e].startswith('.end'):
        p=e
for d in range(len(l)):    
    if l[d].startswith('.ac'):
        m=d
        omega=float(l[m].split('#')[0].split()[-1])#splits the given list at specified character,here gives out frequency
omega =omega*2*3.14159265359

if k == 0 and p == 0:
    print(" invalid file")
    quit()
if m==0:
    print("this is dc circuit")
else:
    print("this is ac circuit")
    m=1
for j in range(len(l)):
    words.append(l[j].split('#')[0].split())  #stores all nodes and values induvidually in words[]
c_list=[]
temp_v=[]
for q in range(k+1,len(words)-(m+1)):# .circuit to .ac
    if words[q][1] not in c_list:
        c_list.append(words[q][1])# nodes
    if words[q][2] not in c_list:
        c_list.append(words[q][2])
    if words[q][0][0] == 'V':
        temp_v.append(words[q][0])#voltages
c_list=c_list+temp_v
print(c_list)
A=np.zeros((len(c_list),len(c_list)),dtype=np.complex_)# create zero array of nxn with complex entities
C=np.zeros((len(c_list),1),dtype=np.complex_)# clist x 1
class components:# create a class
    def __init__(self,words,c_list):#assign values to words and c list
        self.name=words[0]
        if (words[0] in c_list) or words[0][0] =='I':
            self.n1=c_list.index(words[1])
            self.n2=c_list.index(words[2])
            self.value=float(words[m+3])
            self.phase=0
            if words[3] =='ac':
                self.value=self.value/2
                self.phase=float(words[5])
        else:
            self.n1=c_list.index(words[1])
            self.n2=c_list.index(words[2])
            self.value=float(words[3])
        if words[0] in c_list:
            self.k=c_list.index(words[0])
        else:
            k=0
    def Z(self,A,omega):
        n1=self.n1
        n2=self.n2
        if self.name[0] =='C':
            value=complex(0,-(1/(omega*self.value)))
        elif self.name[0] =='L':
            value=complex(0,(omega*self.value))
        else:
            value = self.value
        A[n1,n1]-=(1/value)
        A[n2,n2]-=(1/value)
        A[n1,n2]+=(1/value)
        A[n2,n1]+=(1/value)
        return A
    def v(self,A,C,omega):
        A[self.n1,self.k]=A[self.k,self.n1]=-1
        A[self.n2,self.k]=A[self.k,self.n2]=+1
        C[self.k]=(self.value)*(np.exp(self.phase))
        return A,C
    def i(self,C,omega):
        C[self.n1]+=(self.value)*(np.exp(self.phase))
        C[self.n2]-=(self.value)*(np.exp(self.phase))
        
for t in range(k+1,len(words)-(m+1)):
    q1=components(words[t],c_list)
    if (words[t][0][0] == 'R') or (words[t][0][0] == 'L') or (words[t][0][0] =='C'):
        A=q1.Z(A,omega)
    elif words[t][0][0] == 'V':
        A,C=q1.v(A,C,omega)
    elif words[t][0][0] == 'I':
        C=q1.i(C,freq)
A[c_list.index('GND')]=np.zeros((1,len(c_list)))
A[c_list.index('GND'),c_list.index('GND')]=1

print(A)
print(C)


x = np.linalg.solve(A,C)

print(x)
