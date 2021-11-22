import argparse
import pathlib


def arguments_data():
    parser = argparse.ArgumentParser(description='Unified hypervisor for static analyze python tools')
    parser.add_argument("-p", "--path", type=pathlib.Path,
                        help='Target directory.', )
    parser.add_argument("-o", "--output", type=pathlib.Path,
                        help='Output file.')
    parser.add_argument("-j", "--json", action='store_true', default=False,
                        help='Make output as json.')
    parser.add_argument('-i', '-ignore', nargs='+', dest='blacklist',
                        help='File extensions to ignore.', default=[])
    parser.add_argument('-d', '-depth', type=int, dest='depth',
                        help='Depth for sub-folders (top-level is 0).',
                        default=float('inf'))
    return parser.parse_args()


cli_arguments = arguments_data()
