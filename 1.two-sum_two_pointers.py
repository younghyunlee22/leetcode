def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        n = len(nums)
        l = 0
        r = n - 1
        while(l<r):
            if nums[l] + nums[r] < target:
                l+=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                result.append(l)
                result.append(r)
                l+=1
        return result
    
twoSum([2,7,11,15], 9)
