class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            for l in range(len(local)):
                if local[l] == '+':
                    local = local[:l]
                    break
            local = local.replace('.', '')
            emails[i] = local + '@' + domain
        return len(set(emails))
