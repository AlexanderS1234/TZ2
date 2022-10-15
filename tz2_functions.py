def _min(file):
    f = open(file)
    a = [int(i) for i in f.readline().split()]
    f.close()
    return min(a)

def _max(file):
    f = open(file)
    a = [int(i) for i in f.readline().split()]
    f.close()
    return max(a)

def _sum(file):
    f = open(file)
    a = [int(i) for i in f.readline().split()]
    f.close()
    return sum(a)

def _mult(file):
    f = open(file)
    a = [int(i) for i in f.readline().split()]
    f.close()
    p = 1
    for i in a:
        p *= i
    return p
