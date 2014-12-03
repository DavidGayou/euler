#from ../utils import gcd



def gcd(a, b):
    while b!=0 :
        r = a % b
        a = b
        b = r
    return a

def simplification(a, b):
    c = a
    d = b

    g = gcd(c,d)
    while g != 1:
        c = c/g
        d = d/g
        g = gcd(c,d)
    return (c,d)

def falseSimplification(a, b):
    a0 = a%10
    a1 = a/10
    b0 = b%10
    b1 = b/10


    if a0 == b0:
        return (a1,b1)
    if a0 == b1:
        return (a1,b0)
    if a1 == b1:
        return (a0,b0)
    if a1 == b0:
        return (a0,b1)
    return "Nothing"




result = []
for i in range(10,100):
    for j in range(10,i-1):
        #print "%d/%d" %(j,i)
        #print gcd(j,i)

        ##exclude trivial answers
        if i%10 == 0 and j%10 == 0:
            continue
        
        fs = falseSimplification(j,i)

        if fs is "Nothing":
            continue

        a = fs[0]
        b = fs[1]

        if a==0 or b == 0:
            continue


        if (j+0.0)/a == (i+0.0)/b:
            result.append((j,i))

#########
#Now we have the good fractions
print result

nom = 1
denom = 1
for f in result:
    nom = nom*f[0]
    denom = denom*f[1]

print "%d / %d " % (nom, denom)
print simplification(nom, denom)
