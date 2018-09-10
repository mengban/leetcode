# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = len(nums1)-1
        j = len(nums2)-1
        pos = i+j+1
        cnt = i+j+2
        tmp = [0] * cnt
        tmp[:i+1] = nums1
        if i <0 :
            tmp = nums2
        else:
            while(j>=0):    # 重新排序 O(len(num2))
                if nums2[j]>=nums1[i]:
                    tmp[pos] = nums2[j]
                    j -= 1
                else:
                    if i>=0:                     # num1 还没遍历完
                        tmp[pos] = nums1[i]
                        i -= 1
                    else:                       # num1 已经遍历完了
                        tmp[:pos+1] = nums2[0:j+1] # 直接复制过去
                        j = -1                     # j 置负
                        break
                    
                pos -= 1
        if (cnt)%2==0:  # 偶数个
            media = (tmp[int(cnt/2)]+tmp[int(cnt/2-1)])/2
        else:
            media = tmp[int((cnt-1)/2)]
        return media
        
