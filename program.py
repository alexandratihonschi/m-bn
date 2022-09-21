a=int(input('primul numar este- '))
b=int(input('al doilea numar este- '))
c=int(input('al treilea numar este- '))
#a
def max_div(a, b, c):
    l=[]
    n=0
    for i in range(1, min(a, b, c)+1):
        if a%i==b%i==c%i==0:
            n+=1
            l.append(i)
    return max(l)

print(max_div(a, b, c))
#b 

#c
def vmax(a, b, c):
    return max([a,b,c])
print(vmax(a,b,c))
#d
def vmin(a, b, c):
    return min([a,b,c])
print(vmin(a,b,c))
#e

def div(a, b, c):
    l=[]
    n=0
    for i in range(1, max(a, b, c)+1):
        if a%i==b%i==c%i==0:
            l.append(i)
    return l
print(div(a, b,c ))



