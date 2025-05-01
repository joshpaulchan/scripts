#!/usr/bin/env python3

import os
import random
import argparse

def pick_random_item(parent_directory: str, include_files: bool = True) -> os.PathLike | None:
    # List all subdirectories in the given parent directory
    try:
        subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) or include_files]
        
        if not subdirectories:
            print("No subdirectories found in the specified directory.")
            return None
        
        # Randomly pick one subdirectory
        random_directory = random.choice(subdirectories)
        return os.path.join(parent_directory, random_directory)
    
    except FileNotFoundError:
        print("The specified directory does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Randomly select an item (file or directory) from a parent directory')
    parser.add_argument('parent_dir', help='Path to the parent directory')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output')
    parser.add_argument('-i', '--include-files', action='store_true', help='Include files in the selection')
    parser.add_argument('-n', '--num-tries', type=int, default=3, help='Number of random selections to make')
    args = parser.parse_args()
    
    selection = None
    for i in range(args.num_tries):
        selection = pick_random_item(args.parent_dir, args.include_files)
        
    if not selection:
        exit(1)
        
    if args.verbose:
        print(f"\nFinal selection: {selection}")
    else:
        print(selection)