class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices_list = []
        
        for i_ind, i_val in enumerate(nums):
            for j_ind, j_val in enumerate(nums):
                if i_val + j_val == target and i_ind != j_ind:
                    indices_list.append(i_ind)
                    indices_list.append(j_ind)

                    return indices_list