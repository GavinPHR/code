# Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(x if x != '.' else "[.]" for x in address)