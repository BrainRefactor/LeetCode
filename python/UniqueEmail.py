# https://leetcode.com/problems/unique-email-addresses/
# Every email consists of a local name and a domain name, separated by the
# @sign.
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com
# is the domain name.

# TLDR;


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        helper = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")

            result = "@".join([local, domain])

            if result not in helper:
                helper.add(result)

        return len(helper)
