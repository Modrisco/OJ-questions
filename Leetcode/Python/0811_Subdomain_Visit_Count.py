class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for cp in cpdomains:
            time = int(cp.split()[0])
            full_url = cp.split()[1]
            url_list = full_url.split('.')
            while len(url_list) > 0:
                cur_url = '.'.join(url_list)
                if cur_url in res:
                    res[cur_url] += time
                else:
                    res[cur_url] = time
                url_list = url_list[1:]
        true_res = []
        for key in res:
            true_res.append(str(res.get(key)) + ' ' + key)
        return true_res
