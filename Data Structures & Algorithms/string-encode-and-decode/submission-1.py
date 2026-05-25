class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i)) + "%" + i 
        return encode       

    def decode(self, s: str) -> List[str]:
        L = []
        i=0
        while i < len(s):
            j = s.index("%", i)
            leng = int(s[i:j]) 
            word = s[j+1 : j+1+leng]
            L.append(word)
            i = j+1+leng
        return L
