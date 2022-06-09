import numpy as np
import math


class Bitboard:
    def __init__(self):
        self.empty_bb = np.uint64(0)
        self.full_bb = np.uint64((2**64) - 1)

        self.white_pawns = np.uint64(0x000000000000ff00)
        self.black_pawns = np.uint64(0x00ff000000000000)

        self.white_rooks = np.uint64(0x000000000000081)
        self.black_rooks = np.uint64(0x8100000000000000)

        self.white_bishops = np.uint64(0x000000000000024)
        self.black_bishops = np.uint64(0x2400000000000000)

        self.white_knights = np.uint64(0x000000000000042)
        self.black_knights = np.uint64(0x4200000000000000)

        self.white_queen = np.uint64(0x0000000000000008)
        self.black_queen = np.uint64(0x0800000000000000)

        self.white_king = np.uint64(0x0000000000000010)
        self.black_king = np.uint64(0x1000000000000000)

        self.white_pieces = self.full_bb & self.white_pawns | self.white_bishops | self.white_knights | self.white_rooks | self.white_queen | self.white_king
        self.black_pieces = self.full_bb & self.black_pawns | self.black_bishops | self.black_knights | self.black_rooks | self.black_queen | self.black_king

    def print_current_bitboard(self):
        current_bitboard = np.array(np.binary_repr(
            self.black_pieces | self.white_pieces))
        for x in range(len(current_bitboard)):
            if x + 1 % 8:
                print("")
