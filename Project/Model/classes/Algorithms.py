from numpy.linalg import norm as euclidean
from numpy import array as array
import time

class Algorithms(object):

    def __init__(self):
        pass

    def euclideanDistance(self,a):
        start=time.time()
        c=[]
        res=[]
        z=0
        while(len(a)>z):
            analysis=a.copy()
            del analysis[z]
            for i in analysis:
                res.append(euclidean(array(a[z])-array(i)))
            c.append(tuple( [ a[z],analysis[res.index(min(res))]]))
            res.clear()
            z+=1
        print("--- {} CPU Seconds Elapsed ---".format(time.time()-start))   
        return c
    
    def find(self,target,arr):
        """
        :param target, expecting tuple 
        :param list values  
        :return shortest Euclidean Distance
        """
        t=tuple(target)
        analysis=list(arr)
        del analysis[analysis.index(t)]
        c=[]
        for i in analysis:
            c.append(euclidean(array(t)-array(i)))
        return analysis[c.index(min(c))]

    def binarySearch(self,arr,k):
        """
        O(log * n)
        :param arr: Sorted Array
        :param k: Key for Selection
        :return: Index
        """
        lo=0
        hi=len(arr)-1
        while(hi>=lo):
            mid=(hi+lo)//2
            if(arr[mid] == k):
                return mid
            elif(arr[mid]>k):
                hi-=1
            elif(arr[mid]<k):
                lo-=1
            else:
                return None
