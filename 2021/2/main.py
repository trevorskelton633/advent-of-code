#!/usr/bin/env python3

import os, argparse

def update_pos(pos, direction, amount, use_aim=False):
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

def main(fname, use_aim=False, verbose=False):
    pos = { 'x':0, 'y':0 }

    if use_aim:
        pos['aim'] = 0
    
    if os.path.exists(fname):
        with open(fname) as f:
            for move in f:
                if verbose:
                    print(pos)

                direction, amount = move.split()
                update_pos(pos, direction, int(amount), use_aim)

    print(f"Solution: {pos['x'] * pos['y']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2021  Day 2')
    parser.add_argument('filename')
    parser.add_argument('--aim', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    main(args.filename, args.aim, args.verbose)
