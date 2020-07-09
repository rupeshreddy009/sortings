def bubble_sort(lis):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lis) -1):
            if lis[i]>lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
                sorted = False
    return lis 
