class LFSR:
    def __init__(self, seed, tap):
        self.seed = seed
        self.tap = tap

<<<<<<< HEAD
    def bit(self):
        self.i = self.seed[len(self.seed) - self.tap]

    def step(self):
        xo = int(self.seed[0]) ^ int(self.i)
        self.seed = str(self.seed[1:]) + str(xo)
=======
    def bit(self, i):
        self.i = self.seed[len(self.seed)-self.tap]

    def step(self):
        xo = int(self.seed[0])^int(self.i)
        self.seed = str(self.seed[1:])+str(xo)
>>>>>>> 7619e176330cfe70a2cdcc7994812241e2040df9

    def __str__(self):
        return self

def main():

<<<<<<< HEAD
# your executable code that invokes LFSR
 if __name__ == '__main__':
    main()
initial_seed = ['0110100111', '0100110010', '1001011101', '0001001100', '1010011101']
tap = [2, 8, 5, 1, 7]
for flag in range(len(initial_seed)):
    test = LFSR(initial_seed[flag], tap[flag])
    test.bit()
    test.step()
    print(test.seed, test.seed[-1])
=======
def main():
        
        # your executable code that invokes LFSR
 if __name__ == '__main__':
     lfsr = LFSR()
     initial_seed = ['0110100111',
                     '0100110010',
                     '1001011101',
                     '0001001100',
                     '1010011101']
     tap = [2, 8, 5, 1, 7]
     i = 0
     for each in initial_seed:
         lfsr.initial_seed = initial_seed[i]
         lfsr.tap = tap[i]
         lfsr.step()
         i += 1
         print('test')
>>>>>>> 7619e176330cfe70a2cdcc7994812241e2040df9
