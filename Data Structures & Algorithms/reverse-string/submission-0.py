class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp_value : str = ""
        last_index = len(s) - 1
        index_limit : int = (len(s)//2) 
        for i in range(index_limit):
            temp_value = s[i]
            s[i] = s[last_index-i]
            s[last_index-i] = temp_value
