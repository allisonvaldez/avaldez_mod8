#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:03:34 2022

@author: leebujm1
"""

from PIL import Image as ig
from lfsr import LFSR as L


class ImageEncrypter:

    def __init__(self, lfsr, fileName):
        self.fileName = fileName
        self.lfsr = lfsr

    def pixelate(self):
        with ig.open(self.fileName) as im:
            width = im.width
            height = im.height
            return width, height, im

    def encrypt(self, width, height, im, lfsr):
        for row in range(width):
            for col in range(height):
                pix = im.getpixel((row, col))
                pixE = []
                for chan in pix:
                    q = L.bit()
                    seed = L.step()
                    pixE.append(chan ^ int(seed, 2))
                im.putpixel((row, col), tuple(pixE))
                self.lfsr.seed = L(seed, 5)

        im.save('bruh.png')
        return im


def main():
    if __name__ == "__main__":
        main()


fileName = "/mnt/c/Users/leebujm1/Desktop/football.png"
lfsr = L("10011010", 5)
bruh = ImageEncrypter(lfsr, fileName)
[w, h, im] = bruh.pixelate()
bruh.encrypt(w, h, im, lfsr)