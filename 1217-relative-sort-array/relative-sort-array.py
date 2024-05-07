class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        sorted_lst = []

        for x in arr2:
            while x in arr1:
                sorted_lst.append(x)
                arr1.remove(x)

        return(sorted_lst+sorted(arr1))