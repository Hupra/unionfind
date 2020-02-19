# UnionFind

# Quick find


class QuickFind:

    def __init__(self, n):
        self.id = [x for x in range(n)]

    def union(self, p, q):

        # self.id = [self.id[q] if x == self.id[p] else x for x in self.id]

        p = self.id[p]
        q = self.id[q]

        self.id = [q if (x == p) else x for x in self.id]

        for i in range(len(self.id)):
            if(self.id[i] == p):
                self.id[i] = q

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return len(set(self.id))

    def test(self):
        return self.id
