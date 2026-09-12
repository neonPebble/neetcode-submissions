class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort
        num_length : int = len(nums)
        if num_length == 0:
            return []
        sorted_array : list[int] = [0]
        sorted_array = self.merge_sort(nums, 0, num_length -1)
        return sorted_array
    
    def merge_sort(self,nums: list[int], l: int, r: int) -> List[int]:
        if l==r:
            return [nums[l]]
        m = (l + r) // 2
        
        left_arr = self.merge_sort(nums, l, m)
        l_size = m - l + 1
        right_arr = self.merge_sort(nums, m+1, r)
        r_size = r - m
        final_arr: list[int] = []
        
        i, j = 0, 0
        while i<l_size and j<r_size:
            if left_arr[i]<= right_arr[j]:
                final_arr.append(left_arr[i])
                i+=1
            else:
                final_arr.append(right_arr[j])
                j+=1
        
        while i<l_size:
            final_arr.append(left_arr[i])
            i+=1
        
        while j<r_size:
            final_arr.append(right_arr[j])
            j+=1
        
        return final_arr

