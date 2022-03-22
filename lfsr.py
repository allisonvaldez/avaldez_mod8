class LFSR:
    def __init__(self, seed, tap):
        self.seed = seed
        self.tap = tap

    def bit(self, i):
        self.i = self.seed[len(self.seed)-self.tap]

    def step(self):
        xo = int(self.seed[0])^int(self.i)
        self.seed = str(self.seed[1:])+str(xo)

    def __str__(self):
        return self


def main():
 
 
    if __name__ == "__main__":
        main()

test = LFSR('1010011101',7)
test.bit(2)
test.step()
 
print(test.seed,test.seed[-1])
