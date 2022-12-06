import argparse

parser = argparse.ArgumentParser()    
parser.add_argument(
        '-f', '--filename', default="input.txt", required=False, help="input file"
    )

args = parser.parse_args()
INPUT_FILE = args.filename