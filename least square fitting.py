#PROGRAM TO ELIMINATE DUPLICATES
#BY LALELANI EDDIE NENE
def fun(x, y):
        if x == 0:
                return y
        else:
                return fun(x-1, x+y)
fun(8,15)
