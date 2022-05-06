import math
import sys
import decimal
from decimal import *
import timeit

Pi = Decimal(0)


# ---------------------------------
def calPiBW(Precision):
    global Pi
    print('\nCalculating...\n', end='', flush=True)
    print('Preparing enviroment...\n', end='', flush=True)

    with localcontext() as lc:
        lc.prec = Precision + 10
        print('.', end='', flush=True)
        d = decimal.Decimal
        print('.', end='', flush=True)
        Pi = d(0)
        print('.', end='', flush=True)

        Round = int(math.sqrt(math.sqrt(Precision))) + 3

        y4 = d(0)
        a0 = d(6) - (d(4) * lc.sqrt(d(2)))
        y = lc.sqrt(d(2)) - d(1)

        print('\rPlanned to iterate ', Round - 1, ' rounds.', flush=True)

        for k in range(1, Round):
            print('.', end='', flush=True)

            y4 = lc.sqrt(lc.sqrt((1 - lc.power(y, 4))))
#            y4 = lc.power((1 - y ** 4) , d(0.25))
            y = (1 - y4) / (1 + y4)
            a0 = a0 * lc.power((1 + y), 4) - lc.power(2, (2 * k + 1)) * y * (1 + y + lc.power(y, 2))

        Pi = 1 / a0
    Pi = Decimal(str(Pi)[0:Precision + 2])
    print('\rDone.\n')
    return 0


# ----------------------------------

# ---------------------------------
def calPiBW9(Precision):
    print('Calculating...\n', end='', flush=True)
    print('Preparing enviroment...\n', end='', flush=True)
    global Pi

    with localcontext() as lc:
        lc.prec = Precision + 10
        print('.', end='', flush=True)
        d = decimal.Decimal
        print('.', end='', flush=True)
        Pi = d(0)
        print('.', end='', flush=True)

        a = 1 / d(3)
        print('.', end='', flush=True)
        #exp = 1 / d(3)
        exp = a
        print('.', end='', flush=True)
        r = (lc.sqrt(3) - 1) / d(2)
        print('.', end='', flush=True)
        #s = (1 - r ** 3) ** exp
        s = lc.power((1 - r ** 3), exp) 
        print('.', end='', flush=True)



        # Round = int((lc.log10(Precision)/lc.log10(9))) + 2
        Round = int(math.log10(Precision) / math.log10(9)) + 3

        print('\rPlanned to iterate ', Round, ' rounds.', flush=True)

        for n in range(1, Round):
            print('.', end='', flush=True)
            t = 1 + 2 * r
            u = lc.power((9 * r * (1 + r + r * r)), exp)
            v = t * t + t * u + u * u
            w = 27 * (1 + s + s * s) / v
            a = w * a + (lc.power(d(3), (2 * n - 1))) * (1 - w)
            s = lc.power((1 - r), 3) / ((t + 2 * u) * v)
            r = lc.power((1 - lc.power(s, 3)), exp)

        Pi = 1 / a
    Pi = Decimal(str(Pi)[0:Precision + 2])
    print('\rDone.\n')
    return 0


# ----------------------------------

# ----------------------------------
def calPiCHD(Precision):
    print('Calculating...\n', end='', flush=True)
    print('Preparing enviroment...\n', end='', flush=True)
    global Pi

    with localcontext() as lc:
        lc.prec = Precision + 10
        print('.', end='', flush=True)
        d = decimal.Decimal
        print('.', end='', flush=True)
        Pi = d(0)
        print('.', end='', flush=True)

        M = d(1)
        print('.', end='', flush=True)
        K = d(6)
        print('.', end='', flush=True)
        L = d(13591409)
        print('.', end='', flush=True)
        S = L
        print('.', end='', flush=True)
        X = M
        print('.', end='', flush=True)

        Round = int(Precision / 14) + 5
        print('\rPlanned to iterate ', Round - 1, ' rounds.', flush=True)

        for k in range(1, Round):
            print('.', end='', flush=True)
            M = ((lc.power(K, 3) - 16 * K) * M) // lc.power(k, 3)
            L += d(545140134)
            X *= d(- 262537412640768000)
            S += (M * L) / X
            K += d(12)

        Pi = (d(426880) * lc.sqrt(d(10005))) / S
    Pi = Decimal(str(Pi)[0:Precision + 2])
    print('\rDone.\n')
    return 0


# ----------------------------------
while 1 == 1 :
    
    print("\n---------PyPi 1.01---------\n\nUsing 3 algorithms to caculate Pi in any precision between 0 to 10^9.\n\n")
    print("   1 -> BW quad (Fastest, middle iterates)\n   2 -> CHD (Slower, most itereates)\n   3 -> BW nine (Slowest, least iterates)\n\n")

    inpt = input(
        "Please input 1 to 3 to select algorithm, anything else to exit: ")

    if inpt.isnumeric():
        m = int(inpt)
    else:
        break
    
    if m != 1 and m != 2 and m != 3:
        break


    inpt = input("Precision: ")
    if inpt.isnumeric():
        n = int(inpt)
    else:
        n = 10

    if m == 1:
        print('\n---->  Total time used: ', timeit.timeit('myPi = calPiBW(n)', number=1, globals=globals()), ' Seconds.  <----\n\n')
        file = open('PiBW.txt', 'w')
        file.write(str(Pi))
        file.close()

    elif m == 2:
        print('\n---->   Total time used: ', timeit.timeit('myPi = calPiCHD(n)', number=1, globals=globals()), ' Seconds.  <----\n\n')
        file = open('PiCHD.txt', 'w')
        file.write(str(Pi))
        file.close()

    elif m == 3:
        print('\n---->   Total time used: ', timeit.timeit('myPi = calPiBW9(n)', number=1, globals=globals()), ' Seconds.  <----\n\n')
        file = open('PiBW9.txt', 'w')
        file.write(str(Pi))
        file.close()
    else:
        print("-Program Error-\nPlease check source code!")
