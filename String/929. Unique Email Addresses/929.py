class Solution:
    def numUniqueEmails(self, emails):
        unique_addresses = set()
        for email in emails:
            [local_name, domain_name] = email.split('@')
            local_name_filterred = local_name.split('+')[0].replace('.', '')
            unique_addresses.add(f'{local_name_filterred}@{domain_name}')

        return len(unique_addresses)


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
