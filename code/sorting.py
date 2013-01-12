def bubble_sort (L):
    
    n = len(L)
    
    for i in range(n-1, 0, -1):
        for j in range (1, i):
            if L[j-1] > L[j]:
                L[j-1], L[j] = L[j], L[j-1]
    
    return L
    
def selection_sort (L):
    
    n = len(L) 
    
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if L[j] < L[min]:
                min = j
        L[min], L[i] = L[i], L[min]
            
    return L
