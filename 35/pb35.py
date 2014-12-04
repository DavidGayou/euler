import array

primes = array.array('b', [True]*1000*1000)


def sieve(limit):
    for i in range(2,limit):
        if primes[i]:
            for j in range(i*i, limit,i):
                primes[j]=False


def get_circulars(n):
    digits = []
    a = n
    while a != 0: 
        digits.insert(0,a%10)
        a = a/10

    #Now i have digit
    permutations = []

    c=0
    while c!=n :
        c=0
        first = digits.pop(0)
        digits.append(first)

        for d in digits:
            c = c*10+d
        permutations.append(c);

    return permutations


limit = 1000000
sieve(limit)

#mycnt=0
#myprimes = []
#for t in range(2,limit):
#    if primes[t]:
#        mycnt+=1
#        myprimes.append(t)

#print "Primes computed : %d" % mycnt

results = []
for p in range(2,limit):
    if not primes[p]:
        continue

    isOk = True
    for c in get_circulars(p):
        if not primes[c]:
            isOk = False
            break;
    if isOk:
        results.append(p)

print len(results)
#print results



