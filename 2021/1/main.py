#!/usr/bin/env python3

import os
import argparse


def count_times_data_increased(inputs, verbose=False):
    increased = 0

    if len(inputs) > 0:
        prev = inputs[0]

        if verbose:
            print(f'{prev} (N/A - No previous data yet)')

        for i in inputs[1:]:
            increased = increased + (1 if i > prev else 0)
            prev = i

            if verbose:
                print('{} ({})'.format(i,
                                       'increased' if i > prev else
                                       'decreased' if i < prev else
                                       'no change'))

        return increased


def sum_elements_in_window(inputs, size=3):
    sums = []

    for i in range(len(inputs)):
        window = inputs[i:i+size]
        if len(window) == size:
            sums.append(sum(window))

    return sums
        

def main(filename, windowed=False, verbose=False):
    if os.path.exists(filename):
        with open(filename) as f:
            inputs = list(map(int, f.readlines()))

        if windowed:
            inputs = sum_elements_in_window(inputs)

        increased = count_times_data_increased(inputs, verbose)

        print(f'Number of times increased: {increased}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2021  Day 1')
    parser.add_argument('filename')
    parser.add_argument('--windowed', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    main(args.filename, args.windowed, args.verbose)
