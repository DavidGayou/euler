import sys

def isPalindromic(n):
    myString = str(n)
    myStringInv = myString[::-1]
    for i in range (0, (len(myString)+1)/2 ) :
        if myString[i] != myStringInv[i] :
            return False
    return True

def isPalindromicInBinary(n) :
    myString = bin(int(n))[2::1]
    #myString.tr
    myStringInv = myString[::-1]
    for i in range (0, (len(myString)+1)/2 ) :
        if myString[i] != myStringInv[i] :
            return False
    return True


def testBothPatlyndromy(n) :
    if isPalindromic(n) and isPalindromicInBinary(n):
        print n
        return True
    return False


def pb36() :
    sum = 0
    for i in range(1,1000000):
        if testBothPatlyndromy(i):
            sum += i
    print sum





#isPalindromic(sys.argv[1])
#testBothPatlyndromy(sys.argv[1])
pb36()




