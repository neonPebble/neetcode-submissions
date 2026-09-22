class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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






        