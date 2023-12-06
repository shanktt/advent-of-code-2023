import argparse
import importlib
import sys

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    parser = argparse.ArgumentParser(description='Advent of Code runner')
    parser.add_argument('days', nargs='+', type=int, help='Days to run')
    parser.add_argument('--sample', action='store_true', help='Use sample input')
    
    args = parser.parse_args()

    for day in args.days:
        try:
            # Dynamically import the day module
            day_module = importlib.import_module(f'days.day{day}')

            # Choose the right input file
            input_file = f'inputs/day{day}.txt'
            if args.sample:
                input_file = f'inputs/day{day}.sample.txt'

            # Read inputs and pass them to the day's functions
            inputs = read_input_file(input_file)
            print(f"Results for Day {day}:")
            print("Part 1:", day_module.part1(inputs))
            print("Part 2:", day_module.part2(inputs))

        except (ImportError, FileNotFoundError):
            print(f"Day {day} is not available.", file=sys.stderr)

            

if __name__ == "__main__":
    main()