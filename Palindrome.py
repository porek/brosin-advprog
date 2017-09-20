def Palichecker(A):
    if A == A[::-1]:
        return True
    else:
        return False

for i in range (100,1000):
    for e in range (100,1000):
        A = e*i
        if Palichecker(str(A)) == True:
            print A


#b = [int(p) for p in str(A)]
