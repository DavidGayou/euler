
fact = {}

def factorial(n):
    if n <= 1:
        return 1
    if n in fact :
        return fact[n]
    res = n*factorial(n-1)
    fact[n] = res
    return res

##Double the factorial to store the result
##And keep the tail recursion
#def factorial(n):
#    if n in fact :
#        return fact[n]
#    fact[n] = factorial_r(n)
#    return fact[n]

def getDigits(n):
    a = n
    res = []
    while a != 0:
        res.append(a%10)
        a = a/10
    return res

def digitFactorial(n):
    res = 0
    for d in getDigits(n):
        res = res + factorial(d)
    return res



###Now lets see whats going on

myResult = 0

for i in range(3, 1000000):
    if digitFactorial(i) == i:
        print i
        myResult += i

print myResult
