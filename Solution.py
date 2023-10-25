class Solution(object):
    def firstBadVersion(self, n):
        i = 1
        j = n
        while (i < j):
            pivot = (i+j) // 2
            if (isBadVersion(pivot)):
                j = pivot
            else:
                i = pivot + 1
        return i
