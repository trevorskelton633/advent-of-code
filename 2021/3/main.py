#!/usr/bin/env python3

import os
import argparse
from collections import Counter


def binary_to_int(s):
    return int(s, base=2)


def flip_bits_to_int(s):
    return int(s, base=2) ^ (2 ** len(s) - 1)


def get_bits_in_col(col, data):
    return [bits[col] for bits in data]


def most_common_bit_in_col(col, data):
    counter = Counter(get_bits_in_col(col, data))

    if counter['0'] == counter['1']:
        return '1'

    bit, count = counter.most_common()[0]
    return bit


def least_common_bit_in_col(col, data):
    counter = Counter(get_bits_in_col(col, data))

    if counter['0'] == counter['1']:
        return '0'

    bit, count = counter.most_common()[-1]
    return bit


def filter_bit_in_col(col, bit, data):
    return [x for x in data if x[col] == bit]


def reduce_most_common_bits(data):
    def reduce(l, col=0):
        if len(l) == 0:
            raise Exception('Could not reduce to one value.')
        elif len(l) == 1:
            return l[0]
        elif len(l) == 2:
            return reduce(filter_bit_in_col(col, '1', l), col+1)
        else:
            bit = most_common_bit_in_col(col, l)
            return reduce(filter_bit_in_col(col, bit, l), col+1)

    return reduce(data)


def reduce_least_common_bits(data):
    def reduce(l, col=0):
        if len(l) == 0:
            raise Exception('Could not reduce to one value.')
        elif len(l) == 1:
            return l[0]
        elif len(l) == 2:
            return reduce(filter_bit_in_col(col, '0', l), col+1)
        else:
            bit = least_common_bit_in_col(col, l)
            return reduce(filter_bit_in_col(col, bit, l), col+1)

    return reduce(data)


def parse_report(data, verbose=False):
    if len(data) > 0:
        cols = len(data[0])

        # Calculate power consumption
        gamma_bits = [most_common_bit_in_col(col, data) for col in range(cols)]
        gamma_binary = ''.join(gamma_bits)
        gamma = binary_to_int(gamma_binary)
        # for epsilon, we could use least_common_bit_in_col but that's just a waste of space/time
        epsilon = flip_bits_to_int(gamma_binary)
        power_consumption = gamma * epsilon

        if verbose:
            print(f'Gamma: {gamma}')
            print(f'Epsilon: {epsilon}')

        # Calculate life support
        oxygen = binary_to_int(reduce_most_common_bits(data))
        co2 = binary_to_int(reduce_least_common_bits(data))
        life_support = oxygen * co2

        if verbose:
            print(f'Oxygen Rating: {oxygen}')
            print(f'CO2 Rating: {co2}')

        return power_consumption, life_support


def main(filename,  verbose=False):
    if os.path.exists(filename):
        with open(filename) as f:
            data = [line.rstrip() for line in f]
        
        power, life = parse_report(data, verbose)

        print(f'Power Consumption: {power}')
        print(f'Life Support: {life}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2021  Day 3')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    main(args.filename, args.verbose)
