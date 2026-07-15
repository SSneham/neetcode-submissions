import sys
sys.setrecursionlimit(10000)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(arr,i,j):
            arr[i],arr[j] = arr[j],arr[i]

        def partition(nums,low,high):
            pivot = nums[high]
            i = low-1
            for j in range(low,high):
                if nums[j]<pivot:
                    i += 1
                    swap(nums,i,j)
            swap(nums,i+1,high)
            return i+1

        def quicksort(nums,low,high):
            if low<high:
                pi = partition(nums,low,high)
                quicksort(nums,low,pi-1)
                quicksort(nums,pi+1,high)
        quicksort(nums,0,len(nums)-1)
        return nums