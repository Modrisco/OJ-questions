class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_log = []
        digit_log = []
        for i, log in enumerate(logs):
            temp = log.split(' ')
            if temp[1].isalpha():
                letter_log.append(temp)
            else:
                digit_log.append(temp)
        # sort logs in letter-log by items after the first one
        letter_log = [' '.join(log) for log in (sorted(letter_log, key=lambda x: ' '.join(x[1:])))]
        digit_log = [' '.join(log) for log in digit_log]
        return letter_log + digit_log

    def reorderLogFiles_answer(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)
