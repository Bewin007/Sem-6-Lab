f=open('input.txt','r').read()
q=f.splitlines()
for i in range(len(q)):
    if '#define' in q[i].split():
        fun=q[i].split()[1]
        val=q[i].split()[-1].replace(')','').replace('(','')
        rep=fun[:fun.index('(')]
        continue
    if rep in q[i]:
        temp=q[i][q[i].index('(')+1:q[i].index(')')]
        q[i]=val.replace(val[0],temp)+';'
    print(q[i])