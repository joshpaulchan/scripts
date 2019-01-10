#! usr/bin/env/python
# Cache Enforcer (for Spotify)
# Spotify took away the option for controlling the cache size, so I'm doing it for them.
# Written by Josh Chan

import os
import shutil

# CONSTANTS
TARGET_DIR = "/Users/joshuapaulchan/Library/Caches/com.spotify.client/Data/" # currently, mac only
SIZE_ALLOWANCE = 1 * ( 1024 ^ 3 ) # 4 gb
DEV = bool(os.environ.get('DEV', False))

def log(statement):
    """
    `log(statement)`
    
    Logs something if in development.
    
    @params: statement: str: statement to log
    @returns: none
    """
    if DEV: print(statement)

def total_size(dir_path):
    """
    `total_size(dir_path)`
    
    Calculates the size of a directory recursively
    
    @params: dir_path: str: the directory to calculate the size of
    @returns: total_size: int: int containing the size of the directory in bytes
    """
    total_size = 0
    for path, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(path, f)
            sz = os.path.getsize(fp)
            total_size += sz
            # log("{}, {} bytes".format(f, sz))
    return total_size


def rmdir(dir_path):
    """
    `rmdir(dir_path)`
    
    Recursively remove the directory @ dir_path
    
    @params: dir_path: str: The directory to remove
    @returns: _ : dict: dict containing meta information
        files_removed: int: number of files removed total
        bytes_removed: int: number of bytes removed total
    """
    shutil.rmtree(dir_path, onerror=log)


def main():
    sz = total_size(TARGET_DIR)
    if sz > SIZE_ALLOWANCE:
        rmdir(TARGET_DIR)
        print("Removed {} GB from Spotify's caches".format(sz / (1024 ** 3)))

if __name__ == '__main__':
    main() 
