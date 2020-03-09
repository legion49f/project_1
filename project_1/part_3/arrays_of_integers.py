from random import randint

def getRandomArray(n) -> list:
    """Return an array of N integers with a range one order of magnite larger from the input."""
    arr = []
    power = 0
    _ = n
    while( _ > 0):
        _ = _ // 10
        power+=1
    rand_int_range = 10**power

    while len(arr) != n:
        rand_int = randint(0, rand_int_range)
        if rand_int not in arr:
            arr.append( rand_int )
    
    return arr

def getSortedArray(n) -> list:
    arr = []
    arr.append(n)
    while(n != 0):
        n-=1
        arr.append( n )
    return arr


print( getRandomArray(100) )

# print( getSortedArray(10) )
