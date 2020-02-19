class QuickUnion:

    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]

    def union(self, p, q):

        p_root = self.find(p)
        q_root = self.find(q)

        # hvis de har den samme root, er de allerede connected
        if (p_root == q_root):
            return None

        # sætter en ene til at have den andens root
        self.id[p_root] = q_root

        # count-- da vi nu har et mindre træ
        self.count -= 1

    def find(self, p):

        # Kigger om pointet er forbundet til sig selv,
        # ellers kigger vi på det punkt det er forbundet til
        # vi gør dette indetil vi når "toppen" af træet
        while (p != self.id[p]):
            p = self.id[p]

        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)
