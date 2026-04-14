class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = []
        
        # Adding all the non Zero Number in temp array
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        # Now puting back all the non zero number in the front of array

        for i in range(len(temp)):
            nums[i] = temp[i]

        # Puting Zero back of the array
        for i in range(len(temp), len(nums)):
            nums[i] = 0

        
        