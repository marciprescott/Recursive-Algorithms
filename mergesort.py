def merge(L, L1, L2):
    i = 0
    j = 0
    k = 0
    while (j < len(L1) or (k < len(L2))):
        if j < len(L1):
            if k < len(L2):
            # We are not at end of L1 or L2 so pull smaller value
                if L1[j] < L2[k]:
                    L[i] = L1[j]
                    j += 1
                    
                else:
                    L[i] = L2[k]
                    k += 1
                    
            else:
                # We are at end of L2, so pull from L1
                L[i] = L1[j]
                j += 1
                
        else:
            # We are at the end of L1, so pull from L2
            L[i] = L2[k]
            k +=1
        i += 1
    return
def mergeSort(L):
    n = len(L)
    if n <= 1:
        return
    # Use slicing operation and interger division to form sublists.
    L1 = L[:n//2]
    L2 = L[n//2:]
    # Here is the reciursive part, we are calling mergeSort til base
    #case
    mergeSort(L1)
    mergeSort(L2)
    merge(L, L1, L2)
    return

favorite_foods = ['ham', 'pizza', 'gumbo', 'bbq', 'cookies']
mergeSort(favorite_foods)
print(favorite_foods)
