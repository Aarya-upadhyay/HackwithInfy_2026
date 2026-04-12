class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        a = s.split()

        if len(p) != len(a):
            return False

        h_p = {}
        h_w = {}

        for i in range(len(p)):
            if (p[i] in h_p and h_p[p[i]] != a[i]) or \
            (a[i] in h_w and h_w[a[i]] != p[i]):
                return False

            h_p[p[i]] = a[i]
            h_w[a[i]] = p[i]

        return True


        
