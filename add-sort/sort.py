import random
import time
# bubble sort

class Sort():
    def bubble_sort(self,arr):
        _len = len(arr)
        for j in range(_len-1):
            for i in range(_len-1-j):
                if arr[i+1] > arr[i]:
                    tmp = arr [i+1]
                    arr[i+1] = arr[i]
                    arr[i] = tmp
        return arr
    ## 合并排序
    def merge_sort(self,arr):
        if len(arr)<=1:  # 单个元素 有序  
            return arr
        middle = len(arr)//2  # (l+r)//2有bug
        #print(l,r,arr[:middle])
        left = self.merge_sort(arr[:middle])
        right = self.merge_sort(arr[middle:])
        ret = self.merge(left,right)
        return ret

    def merge(self,left,right):
        results = []
        posl ,posr = 0,0
        while(posl<=len(left)-1 and posr<=len(right)-1):
            if left[posl] < right[posr]:
                results.append(left[posl])
                posl += 1
            else:
                results.append(right[posr])
                posr += 1
        return results+left[posl:]+right[posr:]        #可能会有某个没有遍历完导致while结束

    ## 快速排序
    '''
    其实可以分为两部分 一部分分 一部分治.  先分 再治
    '''
    def quick_sort(self,arr):
        if len(arr) <=1:  # 递归出口
            return arr
        l = []
        r = []
        mid = []
        pivot = arr[0]
        #print(arr)
        for item in arr:
            if item > pivot: 
                r.append(item)
            elif item < pivot:
                l.append(item)
            else:
                mid.append(item)
        retl = self.quick_sort(l)
        retr = self.quick_sort(r)
        return retl+mid+retr

    ###插入排序  可以优化一下 位置交换的太频繁

    def insert_sort(self,arr):
        _len = len(arr)
        for i in range(1,_len):
            if arr[i-1] > arr[i]: #如果比前面的小
                for j in range(0,i):
                    if arr[i-j-1] > arr[i-j]: #交换
                        tmp = arr[i-j]
                        arr[i-j] = arr[i-j-1]
                        arr[i-j-1] = tmp
                    else:
                        break
            else:
                continue
        return arr

    ##希尔排序
    def shell_sort(self,arr):
        _len = len(arr)
        gap = _len//2
        while gap > 0:
            for i in range(gap,_len):
                _val = arr[i]
                j = i
                while(j>=gap and arr[j-gap] > _val): # 需要交换
                    tmp = arr[j-gap]
                    arr[j-gap] = arr[j]
                    arr[j] = tmp
                    j -= gap
                #交换完毕
            gap = gap//2
        return arr

if __name__ == '__main__':
    cnt = 100
    sort = Sort()
    arr = [random.randint(0,cnt) for x in range(cnt)]
    stime = time.time()
    #bubble_sort(arr[:])
    print(time.time()-stime)
    
    stime = time.time()
    sort.merge_sort(arr[:])
    print(time.time()-stime)

    stime = time.time()
    sort.quick_sort(arr[:])
    print(time.time()-stime)

    stime = time.time()
    sort.insert_sort(arr[:])
    print(sort.insert_sort(arr[:]),time.time()-stime)

    stime = time.time()
    sort.shell_sort(arr[:])
    print(sort.shell_sort(arr[:]),time.time()-stime)