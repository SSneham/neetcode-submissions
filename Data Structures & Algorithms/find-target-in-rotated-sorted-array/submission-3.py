class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1

        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target: return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right subarray is sorted
                if nums[mid]<target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1