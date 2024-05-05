# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):

		result = 1
		start, end = 1, n

		while start <= end:

			mid = (start + end) // 2

			if isBadVersion(mid) == False:
				start = mid + 1

			else:
				end = mid - 1
				result = mid

		return result