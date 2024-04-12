class Solution:

    def lowest_common_ancestor(self, p, q):
        seen = set()

        while p:
            seen.add(p)
            p = p.parent

        while q:
            if q in seen:
                return q
            q = q.parent

    def lowest_common_ancestor_optimal(self, p, q):
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            q_copy = q_copy.parent if q_copy else p
            p_copy = p_copy.parent if p_copy else q

        return p_copy


if __name__ == '__main__':
    tests = [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4],
    ]
    for test in tests:
        s = Solution()
        print(s.lowest_common_ancestor(test[0], test[1], test[2]))