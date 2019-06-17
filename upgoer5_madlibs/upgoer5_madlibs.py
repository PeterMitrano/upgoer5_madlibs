#!/usr/bin/env python

import sys
import argparse


def read_input_text(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        stripped = [l.strip("\n") for l in lines]
        return stripped


def read_vocab(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        stripped = [l.strip("\n") for l in lines]
        return stripped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dict_file")
    parser.add_argument("--textfile")

    args = parser.parse_args()
    vocab = read_vocab(args.dict_file)

    if args.textfile:
        input_text = read_input_text(args.textfile)
    else:
        input_text = []
        for line in sys.stdin:
            input_text.append(line)

    madlib = []
    for line in input_text:
        for word in line.split(" "):
            if word.lower() in vocab:
                madlib.append(word)
            else:
                blank = ''.join(['_'] * len(word))
                madlib.append(blank)

    print(' '.join(madlib))


if __name__ == '__main__':
    main()
