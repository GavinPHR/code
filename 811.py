# Subdomain Visit Count
from typing import List
import collections


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            domain_components = domain.split(".")
            for i in range(len(domain_components)):
                counter[".".join(domain_components[i:len(domain_components)])] += count
        ans = []
        for domain, count in counter.items():
            ans.append(" ".join([str(count), domain]))
        return ans

if __name__ == '__main__':
    a = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    s = Solution()
    print(s.subdomainVisits(a))