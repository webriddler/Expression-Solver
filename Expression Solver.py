# # Expression Solver

inp=input("Enter the Expression: ")
fotp=""
notp=""
r=0
n=[]
for a in range(0,len(inp)):
    if inp[a].isdigit()==False:
        if inp[a-(len(inp)-1)].isdigit()==True\ 
        and a-(len(inp)-1)!=0:
            fotp+=inp[a]
        else:
            break              # Only Special Characters
for a in range(0,len(fotp)):
    if ord(fotp[a])==42 or ord(fotp[a])==43\
    or ord(fotp[a])==45 or ord(fotp[a])==47:
        notp+=fotp[a] 
    else:
        break    # Only Arithmetic Operators except "%"
k=0
dgt=""
for a in range(0,len(notp)+1):
    dgt=""
    while k<len(inp) and inp[k].isdigit()==True:
        dgt+=inp[k]
        k+=1
    k+=1
    dgt=int(dgt)
    n.append(dgt)        # Only Operands Figures
k=0
r=n[0]
for a in range(0,len(notp)):
    if ord(notp[a])==43:
        r+=n[a+1]
    elif ord(notp[a])==45:
        r=r-n[a+1]
    elif ord(notp[a])==42:
        r=r*n[a+1]
    elif ord(notp[a])==47:
        r=r/n[a+1]
print(round(r,2))
