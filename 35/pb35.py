

primes = [2,3]

##ONLY WORK IF RUN IN ORDER
def is_prime(n):
    for p in primes:
        if p*p > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True


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


#Sieves
for i in range(4,1000000):
    is_prime(i)
    #if is_prime(i) :
    #    print i

print "Primes computed : %d" % len(primes)
#print primes

results = []
count = 0
for p in primes:
    isOk = True
    count+=1
    if count %1000==0:
        print "%d - %d"%(count, p)
    for c in get_circulars(p):
        if c not in primes:
            isOk = False
            break;
    if isOk:
        results.append(p)

print len(results)
#print results



