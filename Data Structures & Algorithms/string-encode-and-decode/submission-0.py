class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        n = 0
       
        while n < len(strs):
            encoded_string.append(str(len(strs[n])))
            encoded_string.append("#")
            encoded_string.append(strs[n])
            n+=1
        
        ecoded_output = "".join(encoded_string)
        
        return ecoded_output

    def decode(self, s: str) -> List[str]:
        
        decoded_string = []
        n = 0 
        
        while n < len(s):
            j = n

            while s[j] != "#":
                j+=1

            size  = int(s[n:j])
            n = j + 1 
            j = n + size
            decoded_string.append(s[n :j])
            n = j 

        return decoded_string             

            
            
            
