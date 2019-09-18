class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            return (nums2[(len(nums2)-1)//2] + nums2[(len(nums2))//2])/2
        if len(nums2) == 0:
            return (nums1[(len(nums1)-1)//2] + nums1[(len(nums1))//2])/2
        left1, left2 = 0, 0
        right1, right2 = len(nums1), len(nums2)
        while True:
            mid1 = left1 + (right1 - left1 - 1)//2
            val1 = -float('inf') if mid1 < 0 else nums1[mid1]
            mid2 = left2 + (right2 - left2 - 1)//2
            val2 = -float('inf') if mid2 < 0 else nums2[mid2]
            if val1 >= val2:
                if (mid2 + 1 < len(nums2) and val1 <= nums2[mid2 + 1]) or mid2 + 1 == len(nums2):
                    halfCount = mid1 + mid2 + 1
                    realHalf = (len(nums1) + len(nums2) - 1)/2
                    if halfCount == realHalf:
                        another = val1
                    elif halfCount < realHalf:
                        if mid1 + 1 == len(nums1):
                            another = nums2[mid2 + 1]
                        elif mid2 + 1 == len(nums2):
                            another = nums1[mid1 + 1]
                        else:
                            another = min(nums1[mid1 + 1], nums2[mid2 + 1])
                    else:
                        if mid1 == 0:
                            another = val2
                        else:
                            another = max(val2, nums1[mid1 - 1])
                    return (val1 + another)/2
                movedStep = min(right1 - mid1, mid2 - left2 + 1)
                left2 += movedStep
                right1 -= movedStep
            else:
                # if (mid1 + 1 < len(nums1) and nums2[mid2] < nums1[mid1 + 1]) or mid1 + 1 == len(nums1):
                #     return nums2[mid2]

                if (mid1 + 1 < len(nums1) and val2 <= nums1[mid1 + 1]) or mid1 + 1 == len(nums1):
                    halfCount = mid1 + mid2 + 1
                    realHalf = (len(nums1) + len(nums2) - 1)/2
                    if halfCount == realHalf:
                        another = val2
                    elif halfCount < realHalf:
                        if mid2 + 1 == len(nums2):
                            another = nums1[mid1 + 1]
                        elif mid1 + 1 == len(nums1):
                            another = nums2[mid2 + 1]
                        else:
                            another = min(nums1[mid1 + 1], nums2[mid2 + 1])
                    else:
                        if mid2 == 0:
                            another = val1
                        else:
                            another = max(val1, nums2[mid2 - 1])
                    return (val2 + another)/2
                movedStep = min(mid1 - left1 + 1, right2 - mid2)
                left1 += movedStep
                right2 -= movedStep


if __name__ == '__main__':
    obj = Solution()
    # print(obj.findMedianSortedArrays([1, 2], [-1, 3]))
    # print(obj.findMedianSortedArrays([1, 2], [3, 4]))
    print(obj.findMedianSortedArrays([1], [2, 3, 4]))


