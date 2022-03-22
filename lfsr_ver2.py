#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:19:58 2022

@author: leebujm1
"""


class LFSR:
    def __init__(self, seed, tap):
        self.seed = seed
        self.tap = tap

    def bit(self):  # Gives you the tap value
        self.i = self.seed[len(self.seed) - self.tap]
        return self.i

    def step(self):  # Gives you a new pseudorandom seed
        self.xo = int(self.seed[0]) ^ int(self.i)
        self.seed = self.seed[1:] + str(self.xo)
        return self.seed


def main():
    test = LFSR('1010011101', 7)
    test.bit()
    test.step()

    print(test.seed, test.seed[-1])

    if __name__ == "__main__":
        main()