def permu_recur(num):
    if len(num) == 1: #单个元素直接返回
        return [num]
    ret = permu_recur(num[1:])  #[[],[]]
    
    #print(ret)
    _ret = []
    for i in range(len(ret)):
        ret[i].append(num[0]) #放在最后 
        #print('ret:',ret)
        _ret.append(ret[i][:])   #元素在最后
        for j in range(len(ret[i])-1):#遍历交换位置  bug 就是变修改它 边使用它造成的
            tmp = ret[i][len(ret[i])-1-j]  #从倒数第一个元素开始
            ret[i][len(ret[i])-1-j] = ret[i][len(ret[i])-1-j-1]  #前一个元素 赋给当前元素
            ret[i][len(ret[i])-1-j-1] = tmp
            _ret.append(ret[i][:])
        #print('_ret',_ret)
    return _ret
    
print(permu_recur([1,2,3,4]))          
'''            
num = [1,2,3]
for i in range(len(num)):
    num.append(0)
'''

def combination(num):
    if len(num)==1:
        return num
    ret = []
    
    for i in range(len(num)):
        for j in range(len(num)-i):
            ret.append(num[:i]+[num[i+j]])
    return ret
combination([1,2,3,4])
            
    