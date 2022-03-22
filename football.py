#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:03:34 2022
@author: leebujm1
"""

from PIL import Image as ig
from lfsr import LFSR


class ImageEncrypter:

    def __init__(self, lfsr, fileName):
        self.lfsr = lfsr
        self.fileName = fileName

    def pixelate(self, arr, width, height):
        with ig.open(self.fileName) as im:
            arr = ig.load(im)
            width = im.width
            height = im.height
        return arr

    def encrypt(self, arr, width, height):
        tap = 4;
        seed = "10011010"
        for row in len(width):
            for col in len(height):
                pix = arr[row, col]
                for chan in len(pix):
                    out = LFSR(seed, tap)
                    out.bit()
                    out.step()
                    pix[chan] = pix[chan] ^ int(out.seed)
                    seed = out.seed