class LFSR:

    # creating a LFSR with initial state 'seed' and tap 'tap'
    # mapping each character of seed string into an array of integers 0 or 1
    def __init__(self, seed: str, tap: int):
        self.initial_seed = list(map(int, seed))
        self.tap = tap

    # returning the bit at the tap position index i (negative indexing)
    def bit(self, i: int):
        return self.initial_seed[len(self.initial_seed) - self.tap]

    # execute one LFSR iteration & return new rightmost bit as an int
    def step(self):
        tap_bit = self.bit(self.tap)
        output_xor = self.initial_seed.pop(0) ^ tap_bit
        self.initial_seed.append(output_xor)
        return output_xor

    # return string representation of the LFSR
    def __str__(self):
        return ''.join(map(str, self.initial_seed))


# executable code that invokes LFSR
if __name__ == '__main__':

    seeds = [LFSR('0110100111', 2),
             LFSR('0100110010', 8),
             LFSR('1001011101', 5),
             LFSR('0001001100', 1),
             LFSR('1010011101', 7)]

    # iterate each LFSR once using step()
    for lfsr in seeds:
        lfsr_iteration = lfsr.step()
        # print the new seed and the value of the new bit in format [LFSR] [new bit]
        print(lfsr, lfsr_iteration)