#!/usr/bin/env python3

import os
import argparse


def update_position(pos, direction, amount, use_aim=False):
    if direction == 'forward':
        pos['x'] = pos['x'] + amount
        if use_aim:
            pos['y'] = pos['y'] + pos['aim'] * amount
    elif direction == 'up':
        if use_aim:
            pos['aim'] = pos['aim'] - amount
        else:
            pos['y'] = pos['y'] - amount
    elif direction == 'down':
        if use_aim:
            pos['aim'] = pos['aim'] + amount
        else:
            pos['y'] = pos['y'] + amount


def find_final_position(moves, use_aim=False, verbose=False):
    pos = {'x': 0, 'y': 0}

    if use_aim:
        pos['aim'] = 0

    if verbose:
        print(f'Position: {pos}')

    for move in moves:
        direction, amount = move.split()
        update_position(pos, direction, int(amount), use_aim)

        if verbose:
            print(f'Position: {pos}')

    return pos


def main(filename, use_aim=False, verbose=False):
    if os.path.exists(filename):
        with open(filename) as f:
            data = [line.rstrip() for line in f]

        pos = find_final_position(data, use_aim, verbose)

        print(f"Solution: {pos['x'] * pos['y']}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2021  Day 2')
    parser.add_argument('filename')
    parser.add_argument('--aim', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    main(args.filename, args.aim, args.verbose)
