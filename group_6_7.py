#!/usr/bin/env/ python3
"""The program prints a basic multiplication table.
    """
N = 1
while N <= 12:
    M = 1
    while M <= 12:
        print(N, "*", M, "=", N * M)
        M += 1
    N += 1
