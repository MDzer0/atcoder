pin={1:'x',2:'x',3:'x',4:'x',5:'x',6:'x',7:'x',8:'x',9:'x',0:'x'}
a,b=map(int,input().split())
f=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in f:
    pin[i]='.'
for i in s:
    pin[i]='o'

line1=pin[7]+" "+pin[8]+" "+pin[9]+" "+pin[0]+"\n"
line2=""+pin[4]+" "+pin[5]+" "+pin[6]+"\n"
line3=" "+pin[2]+" "+pin[3]+"\n"
line4="  "+pin[1]+"\n"
print(line1,line2,line3,line4)
