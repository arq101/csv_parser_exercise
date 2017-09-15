#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import json

from csv_parser import CsvParser


def main():
    parser = argparse.ArgumentParser(description='Parses data from CSV files')
    parser.add_argument(
        '-d', dest='dir', type=str, required=True, help="specify path to csv file(s) directory")
    args = parser.parse_args()
    try:
        for root_dir, sub_dirs, files in os.walk(args.dir):
            for file in sorted(files):
                print(file)
                parser = CsvParser(os.path.join(root_dir, file))
                output = parser.parse_csv_file()
                print(json.dumps(output), "\n")
    except FileNotFoundError as e:
        raise


if __name__ == '__main__':
    main()
