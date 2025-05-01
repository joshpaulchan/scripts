#!/usr/bin/env python3

import os
import random
import argparse

def pick_random_item(target: str, include_files: bool = True) -> os.PathLike | None:
    # List all subdirectories in the given parent directory
    try:
        subdirectories = [d for d in os.listdir(target) if os.path.isdir(os.path.join(target, d)) or include_files]
        
        if not subdirectories:
            print("No subdirectories found in the specified directory.")
            return None
        
        # Randomly pick one subdirectory
        random_directory = random.choice(subdirectories)
        return os.path.join(target, random_directory)
    
    except FileNotFoundError:
        print("The specified directory does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def main():
    parser = argparse.ArgumentParser(description='Randomly select an item (file or directory) from a parent directory')
    parser.add_argument('dir', nargs='?', default='.', help='Path to the parent directory (defaults to current directory)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output')
    parser.add_argument('-i', '--include-files', action='store_true', help='Include files in the selection')
    parser.add_argument('-n', '--num-tries', type=int, default=3, help='Number of random selections to make')
    parser.add_argument('-r', '--relative-to', default='', help='Base directory to prepend to relative paths')
    args = parser.parse_args()
    
    if args.relative_to:
        target = os.path.join(args.relative_to, args.dir)
    else:
        target = args.dir
    
    if args.verbose:
        print(f"Target: {target}")

    selection = None
    for _ in range(args.num_tries):
        selection = pick_random_item(target, args.include_files)
        
    if not selection:
        exit(1)
        
    if args.verbose:
        print(f"\nFinal selection: {selection}")
    else:
        print(selection)
if __name__ == "__main__":
    main()