import numpy as np

testfile1 = input("Please input testfile1:")
testfile2 = input("Please input testfile2:")
inside_input=input("Please input inside file:")
outside_input=input("Please input outside file:")
inside = np.loadtxt(inside_input)
outside = np.loadtxt(outside_input)

def get_key(testfile):#Split each line into 2 key values
    fr = open(testfile,'r+')
    letter=[]
    for line in fr.readlines():
        line=line.strip('\n')
        word = [line[i:i + 2]  for i in range(0, len(line))]
        letter.append(word)
    return letter

def ca_log(in_out,freq_line):#Caculate the entropy of the eachline
    sum_value=0
    for i in range(4):
        for j in range(4):
            sum_value+=(freq_line[i][j])*(np.log2(in_out[i][j]))
    return sum_value

def ca_ratio(freq_line):#Caculate the log ratio
    x=ca_log(inside,freq_line)
    y=ca_log(outside,freq_line)
    if x-y>1:
        print(x-y,"inside")
    else:
        print(x-y,"outside")

def read2letter(data):# Map the key to eachline and caculate the frequency of 2 letters
    #N = ['A', 'C', 'G', 'T']
    N = 'ACGT'
    m=np.zeros([4,4])
    for xs in data:
        for x in xs:
            for i in range(4):
                for j in range(4):
                    c = N[i] + N[j]
                    if c==x:
                        m[i][j]+=1
        #print(m)
        ca_ratio(m)
        m = np.zeros([4, 4])

read2letter(get_key(testfile1))
read2letter(get_key(testfile2))



