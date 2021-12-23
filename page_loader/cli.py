import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(description='Page-loader')
    parser.add_argument('-o', '--output', dest='output')
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    if not args.output:
        args.output = os.getcwd()
    return args
