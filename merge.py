#merge sort
from random import randint
import time






def merge_sort(nlist): #0
    if len(nlist) > 1: #1
        mid = len(nlist)//2
        lh = nlist[:mid]
        rh = nlist[mid:]
        merge_sort(lh)
        merge_sort(rh)
        i=0
        j=0
        k=0
        #1T
        
        while True:
            if i<len(lh) and j<len(rh): #1T1T
                if lh[i]<rh[j]: #1T1TT
                    nlist[k]=lh[i]
                    i=i+1
                    k=k+1
                    
                else: #1T1TF
                    nlist[k]=rh[j]
                    j=j+1
                    k=k+1
     
            else: #1T1F
                while True:
                    if i<len(lh): #1T1FT
                        nlist[k] = lh[i]
                        i=i+1
                        k=k+1
                        
                    else: #1T1FF
                        while True:
                            if j<len(rh):#1T1FFT
                                nlist[k]=rh[j]
                                j=j+1
                                k=k+1
                                
                            else: #1T1FFF
                                #print(nlist)
                                break
                        break
                break
        
    else: #1F
        #print(nlist)
        pass
    return nlist



