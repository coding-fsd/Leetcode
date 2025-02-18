class Solution:
    def compress(self, chars: List[str]) -> int:
        s = "" 
        read = 0 
        
        while read < len(chars):
            char = chars[read] 
            count = 0  
            
           
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            s += char
            if count > 1:
                s += str(count)
        
        
        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)