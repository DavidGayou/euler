

class irrationalDecimalFraction() {


  var pos = 0
  var i = 1

  var prod = 1

  def getNthDigit( n:Int): Int = {



    while (pos < n) {
      pos = pos + i.toString.length
      i+=1
    }
    var posOfDigit = pos-n
    var x = i
    while (posOfDigit != 0 ) {
      posOfDigit -= 1
      x = x/10
    }

    prod = prod *(x%10)

    x%10

  }



  def getDigits(): Int = {

    getNthDigit(10)
    getNthDigit(100)
    getNthDigit(1000)
    getNthDigit(10000)
    getNthDigit(100000)
    getNthDigit(1000000)


    prod
  }

}
