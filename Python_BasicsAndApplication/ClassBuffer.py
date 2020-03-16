class Buffer:
    def __init__(self):
        self.args = []
        self.s = self.k = 0
    def add(self,*a):
        self.args.extend(a)
        n = len(self.args) // 5 * 5
        while n > 0:
            self.s += self.args[0]
            self.args.pop(0)
            n -= 1
            self.k += 1
            if self.k == 5:
                print(self.s)
                self.s = self.k = 0
    def get_current_part(self):
        return self.args