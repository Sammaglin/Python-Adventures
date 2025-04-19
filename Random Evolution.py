import random
def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(0,100)
    if p==1:
        if (x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'
            
# first this part of code and then def
with open("Data.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,100):
    evolve(x)
print(x)
