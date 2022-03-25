class LFSR:
    """
    This class is in charge of organizing and creating the functions
    necessary for our LFSR project to run.
    """

    def __init__(self, seed: str, tap: int):
        """
        This __init__ method in in charge of creating the initial state
        for 'seed' and tap 'tap'. Eventually it will map each character of
        seed string to an array of integers of either 0 or 1.

        :param seed: The string of characters given in the project
        :param tap: The chosen number given for the component for the XOR
        """
        self.initial_seed = list(map(int, seed))
        self.tap = tap


    def bit(self, i: int):
        """
        This function is in charge of returning the bit at the designated tap
        position (at index i). We utilized negative indexing for this function.

        :param i: The designated int tap position
        :return: The bit at designated tap position
        """
        return self.initial_seed[len(self.initial_seed) - self.tap]

    def step(self):
        """
        This function is in charge of executing only one step of the LFSR
        iteration, and will return the rightmost bit as an integer.

        :return: The rightmost bit (as an integer)
        """
        tap_bit = self.bit(self.tap)
        output_xor = self.initial_seed.pop(0) ^ tap_bit
        self.initial_seed.append(output_xor)
        return output_xor

    def __str__(self):
        """
        This function returns the string representation of the LFSR string
        converted in the previous function.

        :return: String representation of LFSR.
        """
        return ''.join(map(str, self.initial_seed))


if __name__ == '__main__':
    """
    Required code to execute program as a script.
    """

    # Seeds necessary to convert.
    seeds = [LFSR('0110100111', 2),
             LFSR('0100110010', 8),
             LFSR('1001011101', 5),
             LFSR('0001001100', 1),
             LFSR('1010011101', 7)]

    """
    This for loop iterates over each string and performs the LFSR once using 
    the step() function
    """

    for lfsr in seeds:
        lfsr_iteration = lfsr.step()

        """
        This statement prints the new seed and value of the new bit created in 
        the format [LFSR][new bit]
        """
        print(lfsr, lfsr_iteration)

