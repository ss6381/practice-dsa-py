# Databricks Technical 1st round (August 14th, 2024).
# rules = [('ALLOW', '1.2.3.4/24'), ('DENY', '8.8.8.8/0')]
# 
# 0.0.0.0/32
# ip_address -> 0.0.0.0
# suffix -> first 32 bits are immutable.
# there are 8 bits in each subsection of the ip address.

class Solution:

    def access(self, rules, ip_address):
        priority = []
        for allow_deny, rule_address in rules:
            priority.append((allow_deny, self.expand_rule(rule_address)))
        for allow_deny, r in priority:
            if self.in_range(r, ip_address):
                return allow_deny
        return 'DENY'

    def expand_rule(self, rule_address):
        # 0.11111111.0.11110000/32 -> 0.255.0.240/32
        # lower: 0.255.0.240
        # upper: 0.255.0.240
        # 0.255.0.240/0
        # lower: 0.0.0.0
        # upper: 255.255.255.255
        rule_address_split = rule_address.split('/')
        ip_address = rule_address_split[0]
        suffix = int(rule_address_split[1])

        section_step = suffix // 8
        bit_position = suffix % 8

        def bit_bound(ip_split, section_step, bit_index, val):
            ip_split_copy = ip_split.copy()
            address = '{0:08b}'.format(int(ip_split_copy[section_step]))
            shifted_address = address[0:bit_index] + "".join([str(val) for i in range(len(address)-bit_index)])
            ip_split_copy[section_step] = str(int(shifted_address, 2))
            
            # set all subsequent indices in ip_split to 0 or 255
            for i in range(section_step+1,len(ip_split_copy)):
                ip_split_copy[i] = str(255 * val)
            return '.'.join(ip_split_copy)

        ip_split = ip_address.split('.')
        return [
            bit_bound(ip_split, section_step, bit_position, 0), # lower bound
            bit_bound(ip_split, section_step, bit_position, 1)  # upper bound
        ]

    def in_range(self, r, ip_address) -> bool:
        ip_split = ip_address.split('.')
        lower_split = r[0].split('.')
        upper_split = r[1].split('.')
        for i in range(len(ip_split)):
            if (
                int(ip_split[i]) < int(lower_split[i]) or
                int(ip_split[i]) > int(upper_split[i])
            ):
                return False
        return True


if __name__ == '__main__':
    rules = [
        ('ALLOW', '1.2.3.4/31'),
        ('ALLOW', '255.124.53.64/9'),
        ('DENY', '8.8.8.8/0')
    ]
    s = Solution()
    print(s.access(rules, '1.2.3.4'))
    print(s.access(rules, '124.53.56.242'))
    print(s.access(rules, '8.8.8.8'))