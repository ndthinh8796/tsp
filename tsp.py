#!/usr/bin/env python3
from nearest_neighbor import NNHeuristic
from two_opt import TwoOpt
from brute_force import BruteForce
from parse_file import read_csv
from sys import stderr


def main():
    import argparse

    parser = argparse.ArgumentParser(usage='./tsp.py [--algo OPTION] file')

    parser.add_argument('file', type=str, help='csv file')
    parser.add_argument('--algo', metavar='OPTION', const='nearest_neighbor',
                        default='nearest_neighbor',
                        choices=['brute_force', 'two_opt', 'nearest_neighbor'],
                        nargs='?',
                        help='choose from [brute_force, two_opt,' +
                        ' nearest_neighbor]')

    args = parser.parse_args()
    return execute_command(args.algo, args.file)


def execute_command(command, file):
    commands = {
                'brute_force': BruteForce().find_shortest_path,
                'two_opt': TwoOpt().find_shortest_path,
                'nearest_neighbor': NNHeuristic().find_shortest_path
                }
    coordinates_list = read_csv(file)

    if len(coordinates_list) > 10 and command == 'brute_force':
        stderr.write('Brute Force algorithm should only be use for map <='+
                     ' 10 cities\n'+
                     '\033[01;91mBetter options\033[00m: '+
                     'two_opt, nearest_neighbor\n')
        exit(0)

    return commands[command](coordinates_list)


if __name__ == '__main__':
    main()
