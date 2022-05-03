import numpy as np

dnafile = input("Please input DNA sequence:")
hmmfile= input("Please input HMM file:")
#Get transition and emission matrix from hmm file
f2 = open(hmmfile, 'r+')
del_f = f2.readlines()
del del_f[0:2]
dfloat=[]
for line in del_f:
    word = list(map(float,line.split()))
    dfloat.append(word)
transititon_probability = np.array([dfloat[0][0:2], dfloat[1][0:2]])
emission_probability = np.array([dfloat[0][2:6], dfloat[1][2:6]])

#Read sequence file to get number and turn it to uperletter
def readfile(testfile):
    fr = open(testfile, 'r+')
    letter = []
    f1=fr.readlines()
    del f1[0]
    for line in f1:
        line = line.strip('\n')
        for i in range(0, len(line)):
            word = line[i:i + 1]
            letter.append(word)
    return letter


def letter2number(alist):
    new_str=[]
    blist=[blist.upper() for blist in alist]
    for i in range(len(alist)):
        if blist[i]=='A':
            new_str.append(0)
        elif blist[i]=='C':
            new_str.append(1)
        elif blist[i]=='G':
            new_str.append(2)
        elif blist[i]=='T':
            new_str.append(3)
    return new_str


def compute_veterbi(obs, states, start_p, trans_p, emit_p):
    max_p = [[0 for col in range(len(states))] for row in range(len(obs))]#max_p records the maximum probability log of each state at each time
    path = [[0 for col in range(len(states))] for row in range(len(obs))]#Path records the path at which max_p corresponds to the probability
    #   initialization
    for i in range(len(states)):
        max_p[0][i] = start_p[i] + emit_p[state_s[i]][obs[0]]
        path[0][i] = i
    for i in range(1, len(obs)):#开始循环Start loop
        max_item = [0 for i in range(len(states))]
        for j in range(len(states)):#当前状态j的概率
            item = [0 for i in states]
            for k in range(len(states)):#再算上边状态的前驱概率， state[k]为前驱状态
                p = max_p[i - 1][k] +emit_p[states[j]][obs[i]] +trans_p[states[k]][states[j]]
                item[states[k]] = p#记录两个概率
            max_item[states[j]] = max(item)#两个状态中选最大的概率
            path[i][states[j]] = item.index(max(item))#判断当前时刻下哪个状态概率最大，记录其前驱状态
        max_p[i] = max_item#将当前概率记回去
    newpath = []
    p = max_p[len(obs) - 1].index(max(max_p[len(obs) - 1]))##判断最后一个时刻哪个状态的概率最大
    newpath.append(p)
    for i in range(len(obs) - 1, 0, -1):#trace back
        newpath.append(path[i][p])
        p = path[i][p]
    newpath.reverse()
    return newpath





obser=letter2number(readfile(dnafile))
state_s = [0, 1]
start_probability = [0.5, 0.5]
start_probability = np.asarray([0.5, 0.5])
log_tran=np.log(transititon_probability)
log_emit=np.log(emission_probability)
log_start=np.log(start_probability)
result=compute_veterbi(obser, state_s, log_start, log_tran, log_emit)
start1=0
j=0
for i in range(len(result)-1):
    if result[i]==result[i+1]:
        j+=1
    elif result[i]!=result[i+1]:
        if result[i]==0:
            print((start1+1,start1+j+1), " state 1\n")
        else:
            print((start1+1, start1 + j+1), " state 2\n")
        start1=start1+j+1
        j=0
if (start1-1)!=len(result):
    if result[start1] == 0:
        print((start1 + 1, len(result)), " state 1\n")
    else:
        print((start1 + 1, len(result)), " state 2\n")


