class Solution(object):
    # O(N*log(M + N)) time | O(N) space
    def findMedianSortedArrays(self, lst1, lst2):
        """
        :type lst1: List[int]
        :type lst2: List[int]
        :rtype: float
        """
        i = j = 0
        lst = []

        while (i < len(lst1) and j < len(lst2)):
            if (lst1[i] < lst2[j]):
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1

        while (i < len(lst1)):
            lst.append(lst1[i])
            i += 1

        while (j < len(lst2)):
            lst.append(lst2[j])
            j += 1

        if (len(lst) % 2 != 0):
            return lst[len(lst)//2]
        else:
            return (lst[len(lst)//2]+lst[((len(lst))//2)-1])/2.0
