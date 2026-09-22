class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start: int = 0
        # end: int = 0
        # max_size: int = k
        # str_len = len(s)
        # if(str_len <= k):
        #     return str_len
        
        
        
        # i: int = 0
        # while i< str_len:
        #     cmp_char = s[i]
        #     j = i+1
        #     repl_pool = k
        #     cur_size = 1
        #     diff_strt = 0
        #     for j in range(i+1, str_len,1):
        #         if s[j] != cmp_char:
        #             repl_pool = repl_pool - 1
                
        #         if repl_pool == k-1:
        #             diff_strt = j-i-1
                
        #         if repl_pool < 0:
        #             break
                
        #         cur_size += 1
            
        #     if cur_size > max_size:
        #         max_size = cur_size
        #     i = i + diff_strt + 1
        # return max_size


        max_wndw : int = 0
        str_len : int = len(s)
        if str_len <=k:
            return str_len
        
        
        left : int = 0
        freq_store : dict[str, int]= {}
        max_freq = 0  # This is not current max but historical max

        for right in range(str_len):
            cur_char = s[right]
            freq_store[cur_char] = freq_store.get(cur_char, 0) + 1
            max_freq = max(freq_store[cur_char], max_freq)

            if (right - left + 1 - max_freq) > k :
                left_char = s[left]
                freq_store[left_char] -=1
                left += 1
            
            max_wndw = max( max_wndw, right-left+1 )
        
        return max_wndw






        