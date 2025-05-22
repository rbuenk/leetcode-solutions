class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_nums = list(set(nums))
        lenghth = len(list_nums)
        missing = 0

        if list_nums[0] == 1:
            return 0
        
        if list_nums[lenghth-1] == lenghth-1:
            return lenghth

        for i, val in enumerate(list_nums):
            if i != val:
                missing = val - 1  
                return missing

        # sum_i = 0
        # sum_v = 0

        # for i, v in enumerate(nums):
        #     sum_i += i + 1
        #     sum_v += v

        #     print "Index ", i,  "Value ", v ,"sum_i = ", sum_i, "sum_v = ", sum_v
        
        # return sum_i - sum_v
