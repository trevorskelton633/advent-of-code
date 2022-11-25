#!/usr/bin/env python3

import os
import argparse


def main(filename,  verbose=False):
    if os.path.exists(filename):
        with open(filename) as f:
            data = [line.rstrip() for line in f]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2021  Day N')
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    main(args.filename, args.verbose)
