class Solution:
    def defangIPaddr(self, address: str) -> str:
        ipStr = address.replace('.','[.]')
        return ipStr
        