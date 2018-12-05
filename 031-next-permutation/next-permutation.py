# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#


## 字典序法
# 1.从右往左 找出第一个 a(i-1)<a(i)   i-1
# 2.从右往左 找出第一个 a(i-1) < a(j) j
# 3.交换 a(i-1)与a(j)
# 4.逆序 a(i+1:)
## a = a + b
## b = a - b
## a = a - b
##有bug...
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        if len_ > 1:
            posa = -1
            posb = -1
            for i in range(len(nums)): #find a
                if nums[len_ -1- i] > nums[len_-1-i-1]:
                    posa = len_-1-i-1
                    break
            if posa != -1:# 不是刚好全逆序
                for i in range(len(nums)): #find b
                    if nums[posa] < nums[len_-1-i]:
                        posb = len_-1-i
                        break
                #交换值
                print(posa,posb)
                if posa!=posb:
                    nums[posa] = nums[posa] + nums[posb]
                    nums[posb] = nums[posa] - nums[posb]
                    nums[posa] = nums[posa] - nums[posb]

                first = posa + 1
                last = posa + len(nums[posa+1:]) 
            else:
                print(nums)
                first = 0
                last = len_ -1
            
            while(last>first):
                print(nums)
                tmp = nums[first]
                nums[first] = nums[last]
                nums[last] = tmp 
                first += 1
                last -= 1
            
                
        
