

class WeightedQuickUnion:

    def __init__(self, n):
        # Hvor mange træer vi har
        self.count = n
        # id fortæller hvad punktet er forbundet til.
        # hvis fx. id[0] == 0 vil dette punkt være forbundet til sig selv.
        self.id = [x for x in range(n)]
        # sz er størrelsen på træet
        # altså: hvor mange elementer der er forbundet til dette punkt
        self.sz = [1 for x in range(n)]

    def union(self, p, q):

        p_root = self.find(p)
        q_root = self.find(q)

        # Hvis de har den samme root, har vi ikke brug for at ændre noget
        if(p_root == q_root):
            return

        # Kigger hvilket træ er lavest og forbinder det til det største.
        # Størelsen på et træ er defineret ud fra hvor mange elemeneter
        # det består af, og ikke hvor "højt" der rent faktisk er.
        if self.sz[p_root] < self.sz[q_root]:

            # Sætter p_root til q_root da p_root er mindst og
            # defor skal sættes til det q_root da det er strørre
            self.id[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]

        else:
            self.id[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]

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
