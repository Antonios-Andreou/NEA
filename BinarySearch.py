def binary_search(nlist, n):
    if len(nlist) > 1:
        mid = len(nlist)//2
        if nlist[mid] < n:
            nlist = nlist[mid:]
            binary_search(nlist, n)
        elif nlist[mid] > n:
            nlist = nlist[:mid]
            binary_search(nlist, n)
        else:
            print("Found within list")
    else:
        if nlist[0] == n:
            print("Found within list")
        else:
            print("Not in list")
