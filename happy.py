
def numSquareSum(n):
    squareSum = 0
    while (n != 0):
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum

def isHappyNumber(n):
    st = set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n in st:
            return False
        st.add(n)


print(isHappyNumber(20))  
