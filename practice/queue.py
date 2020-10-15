class Queue:
    def __init__(self):
        self.q = []
    
    def __str__(self):
        p = str(self.q)
        return p

    def push(self, value):
        self.q.append(value)
        return None

    def __len__(self):
        return len(self.q)

    def dd(self):
        return self.q.pop(0)

    def vazio(self):
        return len(self.q) == 0

