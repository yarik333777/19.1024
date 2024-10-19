from math import inf

def true_divide(first, second):
    groop  = float(first)
    loon = float(second)
    if groop != 0 and loon  != 0:
        return groop / loon
    else:
        return inf
j = true_divide(6,0)
print(j)